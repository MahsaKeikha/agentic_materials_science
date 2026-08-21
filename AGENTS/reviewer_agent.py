"""Performs final scientific quality and human review handoff."""

def run(context: dict) -> dict:
    return {"agent": "reviewer", "status": "review_required", "context": context}
