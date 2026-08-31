"""Real GenLayer Direct Mode coverage for deterministic ENDLINE lifecycle paths."""
import pytest

CONTRACT = "contracts/endline.py"
SOURCES = ("https://example.com", "https://www.iana.org", "https://www.iana.org/domains/example")

def register(contract, key="endline:direct"):
    return contract.register_dependency("Direct dependency", "API", "v1", key, *SOURCES)

def test_registers_and_persists_source_set(direct_deploy, direct_vm, direct_owner):
    direct_vm.warp("2026-01-02T03:04:05Z")
    contract = direct_deploy(CONTRACT)
    assert register(contract) == 1
    dep = contract.get_dependency(1)
    assert dep["creator"] == direct_owner.as_hex
    assert dep["source_version"] == 1 and dep["assessment_count"] == 0 and dep["is_stale"]
    assert contract.get_source_set(1, 1)["source_urls"] == list(SOURCES)

@pytest.mark.parametrize("kind", ["API", "SDK", "MODEL", "PACKAGE", "PROTOCOL", "SERVICE", "OTHER"])
def test_each_allowed_kind_registers(direct_deploy, kind):
    contract = direct_deploy(CONTRACT)
    assert contract.register_dependency("Dependency", kind, "v1", "k:" + kind.lower(), *SOURCES) == 1

@pytest.mark.parametrize("bad", ["", "api", "WEB", "UNKNOWN"])
def test_invalid_kind_reverts(direct_deploy, direct_vm, bad):
    contract = direct_deploy(CONTRACT)
    with direct_vm.expect_revert():
        contract.register_dependency("Dependency", bad, "v1", "bad:" + (bad or "empty"), *SOURCES)

@pytest.mark.parametrize("url", ["http://example.com", "https://localhost", "https://127.0.0.1", "https://10.0.0.1", "https://user:pass@example.com"])
def test_unsafe_primary_source_reverts(direct_deploy, direct_vm, url):
    contract = direct_deploy(CONTRACT)
    with direct_vm.expect_revert():
        contract.register_dependency("Dependency", "API", "v1", "unsafe:" + str(len(url)), url, SOURCES[1], SOURCES[2])

def test_duplicate_is_publisher_scoped(direct_deploy, direct_vm, direct_bob):
    contract = direct_deploy(CONTRACT)
    register(contract, "same")
    with direct_vm.expect_revert():
        register(contract, "same")
    with direct_vm.prank(direct_bob):
        assert register(contract, "same") == 2

def test_source_update_is_immutable_and_creator_only(direct_deploy, direct_vm, direct_bob):
    contract = direct_deploy(CONTRACT)
    register(contract)
    old = contract.get_source_set(1, 1)
    with direct_vm.prank(direct_bob):
        with direct_vm.expect_revert():
            contract.update_sources(1, "https://example.org", SOURCES[1], SOURCES[2])
    contract.update_sources(1, "https://example.org", "https://www.iana.org/help", "https://www.iana.org/about")
    assert contract.get_dependency(1)["source_version"] == 2
    assert contract.get_dependency(1)["is_stale"]
    assert contract.get_source_set(1, 1) == old
    assert contract.get_source_set(1, 2)["source_urls"][0] == "https://example.org"
