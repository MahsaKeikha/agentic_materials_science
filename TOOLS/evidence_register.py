"""Tracks evidence and source provenance."""

def run(records):
    return [{"record": r, "verified": False} for r in records]
