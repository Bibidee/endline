"""Deterministic admission and classifier-output policy shared by tests and contract design."""
import ipaddress
from datetime import date
from urllib.parse import urlparse

KINDS = frozenset(("API", "SDK", "MODEL", "PACKAGE", "PROTOCOL", "SERVICE", "OTHER"))
STATUSES = frozenset(("ACTIVE", "DEPRECATED", "SECURITY_ONLY", "END_OF_LIFE", "REPLACED", "UNKNOWN"))
REASONS = frozenset(("NO_CHANGE_NOTICE", "OFFICIAL_DEPRECATION_NOTICE", "SECURITY_MAINTENANCE_ONLY", "RETIREMENT_ANNOUNCED", "RETIREMENT_EFFECTIVE", "SUCCESSOR_IDENTIFIED", "CONFLICTING_EVIDENCE", "INSUFFICIENT_EVIDENCE", "UNCLASSIFIED"))
EVIDENCE = frozenset(("SUFFICIENT", "AMBIGUOUS", "INSUFFICIENT"))

def valid_url(value: str) -> bool:
    if not isinstance(value, str) or len(value) > 500: return False
    try:
        p = urlparse(value)
        if p.scheme != "https" or not p.hostname or p.username or p.password: return False
        host = p.hostname.rstrip(".").lower()
        if host == "localhost" or host.endswith(".local"): return False
        try:
            ip = ipaddress.ip_address(host)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_unspecified or ip.is_multicast or ip.is_reserved: return False
        except ValueError:
            pass
        return True
    except ValueError:
        return False

def normalise(value: str) -> str: return " ".join(value.split())

def valid_date(value: str) -> bool:
    if value == "": return True
    if len(value) != 10 or value[4] != "-" or value[7] != "-": return False
    try: date.fromisoformat(value); return True
    except ValueError: return False

def validate_result(value: object) -> dict:
    if not isinstance(value, dict): raise ValueError("result must be an object")
    required = ("status","effective_date","replacement","migration_required","breaking_change","reason_code","evidence_state","summary")
    if any(k not in value for k in required): raise ValueError("missing result field")
    if not all(isinstance(value[k], str) for k in ("status", "effective_date", "replacement", "reason_code", "evidence_state", "summary")): raise ValueError("invalid string")
    if not isinstance(value["migration_required"], bool) or not isinstance(value["breaking_change"], bool): raise ValueError("invalid boolean")
    result = dict(value)
    result["status"] = result["status"].strip().upper()
    result["reason_code"] = result["reason_code"].strip().upper()
    result["evidence_state"] = result["evidence_state"].strip().upper()
    result["effective_date"] = result["effective_date"].strip()
    result["replacement"] = normalise(result["replacement"])
    result["summary"] = normalise(result["summary"])
    if result["status"] not in STATUSES or result["reason_code"] not in REASONS or result["evidence_state"] not in EVIDENCE: raise ValueError("invalid enum")
    if not valid_date(result["effective_date"]): raise ValueError("invalid date")
    if len(result["replacement"]) > 160 or len(result["summary"]) > 320: raise ValueError("field too long")
    if result["evidence_state"] == "INSUFFICIENT" and (result["status"] != "UNKNOWN" or result["reason_code"] != "INSUFFICIENT_EVIDENCE"): raise ValueError("insufficient evidence invariant")
    if result["evidence_state"] == "AMBIGUOUS" and result["status"] == "ACTIVE": raise ValueError("ambiguous evidence invariant")
    if result["reason_code"] == "RETIREMENT_EFFECTIVE" and result["status"] != "END_OF_LIFE": raise ValueError("retirement invariant")
    if result["reason_code"] == "SECURITY_MAINTENANCE_ONLY" and result["status"] != "SECURITY_ONLY": raise ValueError("security invariant")
    if result["status"] == "REPLACED" and not result["replacement"]: raise ValueError("replacement requires successor")
    return result
