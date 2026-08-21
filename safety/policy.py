"""F83 safety policy."""

def check(context: dict) -> dict:
    return {"allowed": True, "human_review_required": True, "prohibited": ["fabricated evidence", "unreviewed consequential execution"]}
