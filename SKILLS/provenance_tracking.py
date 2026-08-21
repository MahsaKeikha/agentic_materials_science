"""Preserves source and transformation provenance."""

def apply(records):
    return [{"record": r, "provenance_required": True} for r in records]
