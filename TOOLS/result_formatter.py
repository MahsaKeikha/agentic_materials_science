"""Formats reviewable structured results."""

def run(result: dict) -> dict:
    return {"result": result, "review_ready": True}
