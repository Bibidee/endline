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
    status, reason, evidence = result["status"], result["reason_code"], result["evidence_state"]
    date_value, replacement = result["effective_date"], result["replacement"]
    if evidence == "INSUFFICIENT":
        if status != "UNKNOWN" or reason != "INSUFFICIENT_EVIDENCE": raise ValueError("insufficient evidence invariant")
    elif evidence == "AMBIGUOUS":
        if status != "UNKNOWN" or reason != "CONFLICTING_EVIDENCE": raise ValueError("ambiguous evidence invariant")
    elif status == "ACTIVE":
        if reason != "NO_CHANGE_NOTICE" or date_value or replacement or result["migration_required"] or result["breaking_change"]: raise ValueError("active compatibility invariant")
    elif status == "DEPRECATED":
        if reason not in ("OFFICIAL_DEPRECATION_NOTICE", "RETIREMENT_ANNOUNCED") or (reason != "RETIREMENT_ANNOUNCED" and date_value): raise ValueError("deprecation compatibility invariant")
    elif status == "SECURITY_ONLY":
        if reason != "SECURITY_MAINTENANCE_ONLY" or date_value or replacement: raise ValueError("security compatibility invariant")
    elif status == "END_OF_LIFE":
        if reason != "RETIREMENT_EFFECTIVE" or not date_value: raise ValueError("retirement compatibility invariant")
    elif status == "REPLACED":
        if reason != "SUCCESSOR_IDENTIFIED" or not replacement: raise ValueError("replacement compatibility invariant")
    elif reason != "UNCLASSIFIED" or date_value or replacement or result["migration_required"] or result["breaking_change"]: raise ValueError("unknown compatibility invariant")
    return result
