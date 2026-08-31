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
    if value["status"] not in STATUSES or value["reason_code"] not in REASONS or value["evidence_state"] not in EVIDENCE: raise ValueError("invalid enum")
    if not isinstance(value["migration_required"], bool) or not isinstance(value["breaking_change"], bool): raise ValueError("invalid boolean")
    if not all(isinstance(value[k], str) for k in ("effective_date","replacement","summary")) or not valid_date(value["effective_date"]): raise ValueError("invalid string/date")
    if len(value["replacement"]) > 160 or len(value["summary"]) > 320: raise ValueError("field too long")
    if value["evidence_state"] == "INSUFFICIENT" and value["status"] != "UNKNOWN": raise ValueError("insufficient evidence must be unknown")
    if value["evidence_state"] == "AMBIGUOUS" and value["status"] == "ACTIVE": raise ValueError("ambiguous evidence cannot be active")
    if value["reason_code"] == "RETIREMENT_EFFECTIVE" and value["status"] == "ACTIVE": raise ValueError("retirement cannot be active")
    if value["reason_code"] == "SECURITY_MAINTENANCE_ONLY" and value["status"] != "SECURITY_ONLY": raise ValueError("security reason mismatch")
    return {**value, "replacement": normalise(value["replacement"]), "summary": normalise(value["summary"])}
