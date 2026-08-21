"""Keeps conclusions traceable to explicit evidence."""

def apply(claims):
    return [{"claim": c, "evidence_required": True} for c in claims]
