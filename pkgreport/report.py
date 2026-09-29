"""Summarise package release records for the weekly platform report.

A record looks like:
    {"name": "requests", "versions": ["2.31.0", "2.32.0"], "size": 63_488,
     "share": 0.4127, "released": "2026-09-01T12:00:00Z"}
"""
from dateutil.parser import isoparse
from fmtlib import human_bytes, percent
from packaging.version import parse as parse_version


def latest_version(versions: list) -> str:
    """Highest version by PEP 440 ordering, so '1.10' beats '1.9'."""
    return max(versions, key=parse_version)


def summarize(record: dict) -> str:
    """One report line for a package record."""
    released = isoparse(record["released"]).date().isoformat()
    return (
        f"{record['name']} {latest_version(record['versions'])}: "
        f"{human_bytes(record['size'])}, {percent(record['share'])} of downloads, released {released}"
    )


def report(records: list) -> str:
    """Report lines, most downloaded package first."""
    return "\n".join(summarize(r) for r in sorted(records, key=lambda r: -r["share"]))
