import json
from datetime import datetime, timezone
from pathlib import Path


def log_recommendation(
    user_prefs,
    recommendations,
    explanation_mode,
    path="evidence/recommendation_log.jsonl"
):
    """
    Save each recommendation run as a structured
    JSONL event.
    """

    destination = Path(path)

    destination.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    event = {
        "timestamp_utc": (
            datetime.now(
                timezone.utc
            ).isoformat()
        ),

        "preferences": user_prefs,

        "recommendations": [
            {
                "title": song["title"],
                "artist": song["artist"],
                "score": score
            }
            for song, score, _ in recommendations
        ],

        "explanation_mode": explanation_mode
    }

    with destination.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            json.dumps(event)
            + "\n"
        )