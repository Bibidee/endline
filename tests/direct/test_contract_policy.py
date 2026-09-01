import pytest
from contracts.policy import valid_url, valid_date, normalise, validate_result

@pytest.mark.parametrize("url", ["https://example.com", "https://docs.example.com/path?q=1"])
def test_public_https_urls_are_accepted(url): assert valid_url(url)

@pytest.mark.parametrize("url", ["", "http://example.com", "https://", "https://user:pass@example.com", "https://localhost/x", "https://x.local/x", "https://127.0.0.1/x", "https://10.0.0.1/x", "https://172.16.0.1/x", "https://192.168.1.1/x", "https://169.254.1.1/x", "https://[::1]/x", "https://[::]/x", "https://224.0.0.1/x"])
def test_unsafe_urls_are_rejected(url): assert not valid_url(url)

@pytest.mark.parametrize("value", ["", "2026-01-01", "2000-02-29", "2026-12-31"])
def test_valid_dates(value): assert valid_date(value)

@pytest.mark.parametrize("value", ["2026-1-01", "2026-13-01", "2026-02-29", "yesterday", "20260101"])
def test_invalid_dates(value): assert not valid_date(value)

def result(**overrides):
    value={"status":"ACTIVE","effective_date":"","replacement":"","migration_required":False,"breaking_change":False,"reason_code":"NO_CHANGE_NOTICE","evidence_state":"SUFFICIENT","summary":"supported"}; value.update(overrides); return value

def test_result_accepts_active(): assert validate_result(result())["status"] == "ACTIVE"
def test_result_accepts_deprecated(): assert validate_result(result(status="DEPRECATED",reason_code="OFFICIAL_DEPRECATION_NOTICE"))["status"] == "DEPRECATED"
def test_result_accepts_replaced(): assert validate_result(result(status="REPLACED",reason_code="SUCCESSOR_IDENTIFIED",replacement="v2"))["replacement"] == "v2"
def test_result_accepts_security_only(): assert validate_result(result(status="SECURITY_ONLY",reason_code="SECURITY_MAINTENANCE_ONLY"))["status"] == "SECURITY_ONLY"
def test_result_accepts_eol(): assert validate_result(result(status="END_OF_LIFE",reason_code="RETIREMENT_EFFECTIVE",effective_date="2026-01-01"))["status"] == "END_OF_LIFE"
def test_result_accepts_unknown(): assert validate_result(result(status="UNKNOWN",reason_code="INSUFFICIENT_EVIDENCE",evidence_state="INSUFFICIENT"))["status"] == "UNKNOWN"
@pytest.mark.parametrize("field", ["status","effective_date","replacement","migration_required","breaking_change","reason_code","evidence_state","summary"])
def test_missing_required_field_rejected(field):
    value=result(); del value[field]
    with pytest.raises(ValueError): validate_result(value)
@pytest.mark.parametrize("status", ["BROKEN", "", "ACTIVELY_SUPPORTED"])
def test_invalid_status_rejected(status):
    with pytest.raises(ValueError): validate_result(result(status=status))
@pytest.mark.parametrize("reason", ["BROKEN", "", "ACTIVE"])
def test_invalid_reason_rejected(reason):
    with pytest.raises(ValueError): validate_result(result(reason_code=reason))
@pytest.mark.parametrize("evidence", ["BROKEN", "", "UNCERTAIN"])
def test_invalid_evidence_rejected(evidence):
    with pytest.raises(ValueError): validate_result(result(evidence_state=evidence))
@pytest.mark.parametrize("value", [1, None, "true", []])
def test_wrong_migration_type_rejected(value):
    with pytest.raises(ValueError): validate_result(result(migration_required=value))
@pytest.mark.parametrize("value", [1, None, "false", []])
def test_wrong_breaking_type_rejected(value):
    with pytest.raises(ValueError): validate_result(result(breaking_change=value))
def test_oversized_summary_rejected():
    with pytest.raises(ValueError): validate_result(result(summary="x"*321))
def test_oversized_replacement_rejected():
    with pytest.raises(ValueError): validate_result(result(replacement="x"*161))
def test_ambiguous_active_rejected():
    with pytest.raises(ValueError): validate_result(result(evidence_state="AMBIGUOUS"))
def test_insufficient_deprecated_rejected():
    with pytest.raises(ValueError): validate_result(result(status="DEPRECATED", evidence_state="INSUFFICIENT"))
def test_insufficient_requires_its_reason_code():
    with pytest.raises(ValueError): validate_result(result(status="UNKNOWN", evidence_state="INSUFFICIENT"))
def test_retirement_active_rejected():
    with pytest.raises(ValueError): validate_result(result(reason_code="RETIREMENT_EFFECTIVE"))
def test_retirement_requires_end_of_life():
    with pytest.raises(ValueError): validate_result(result(status="DEPRECATED", reason_code="RETIREMENT_EFFECTIVE"))
def test_security_reason_requires_security_status():
    with pytest.raises(ValueError): validate_result(result(reason_code="SECURITY_MAINTENANCE_ONLY"))
def test_replaced_requires_a_successor():
    with pytest.raises(ValueError): validate_result(result(status="REPLACED", reason_code="SUCCESSOR_IDENTIFIED"))
def test_consensus_whitespace_normalises(): assert validate_result(result(status="REPLACED", reason_code="SUCCESSOR_IDENTIFIED", replacement="  Responses   API "))["replacement"] == "Responses API"
@pytest.mark.parametrize("overrides", [
    {"reason_code":"RETIREMENT_ANNOUNCED"},
    {"replacement":"successor"},
    {"effective_date":"2026-01-01"},
    {"migration_required":True},
    {"breaking_change":True},
])
def test_active_compatibility_matrix_rejects_incompatible_fields(overrides):
    with pytest.raises(ValueError): validate_result(result(**overrides))
@pytest.mark.parametrize("overrides", [
    {"status":"SECURITY_ONLY", "reason_code":"OFFICIAL_DEPRECATION_NOTICE"},
    {"status":"END_OF_LIFE", "reason_code":"RETIREMENT_EFFECTIVE"},
    {"status":"REPLACED", "reason_code":"SUCCESSOR_IDENTIFIED", "replacement":"v2", "effective_date":"2026-01-01"},
    {"status":"UNKNOWN", "reason_code":"CONFLICTING_EVIDENCE", "evidence_state":"SUFFICIENT"},
    {"status":"UNKNOWN", "reason_code":"UNCLASSIFIED", "evidence_state":"AMBIGUOUS"},
])
def test_lifecycle_compatibility_matrix_rejects_impossible_combinations(overrides):
    with pytest.raises(ValueError): validate_result(result(**overrides))
def test_summary_whitespace_normalises(): assert validate_result(result(summary="  stable   evidence "))["summary"] == "stable evidence"
def test_contract_style_enum_normalisation():
    outcome = validate_result(result(status=" active ", reason_code=" no_change_notice ", evidence_state=" sufficient "))
    assert (outcome["status"], outcome["reason_code"], outcome["evidence_state"]) == ("ACTIVE", "NO_CHANGE_NOTICE", "SUFFICIENT")
