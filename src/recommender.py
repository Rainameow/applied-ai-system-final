import csv
from typing import Dict, List, Tuple


def load_songs(csv_path: str) -> List[Dict]:
    """Load and normalize the music catalog."""
    songs = []

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"].strip().lower(),
                "mood": row["mood"].strip().lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def retrieve_candidates(
    user_prefs: Dict,
    songs: List[Dict],
    limit: int = 10
) -> List[Dict]:
    """
    Retrieve the most relevant songs before final ranking.

    This is the retrieval part of the applied AI system.
    """

    preferred_genre = user_prefs.get("genre", "").strip().lower()
    preferred_mood = user_prefs.get("mood", "").strip().lower()

    target_energy = float(
        user_prefs.get("energy", 0.5)
    )

    target_tempo = float(
        user_prefs.get("tempo_bpm", 100)
    )

    candidates = []

    for song in songs:
        retrieval_score = 0.0

        if preferred_genre:
            if song["genre"] == preferred_genre:
                retrieval_score += 3.0

        if preferred_mood:
            if song["mood"] == preferred_mood:
                retrieval_score += 2.0

        energy_similarity = max(
            0.0,
            1.0 - abs(
                song["energy"] - target_energy
            )
        )

        retrieval_score += energy_similarity

        tempo_similarity = max(
            0.0,
            1.0 - abs(
                song["tempo_bpm"] - target_tempo
            ) / 100
        )

        retrieval_score += tempo_similarity

        candidates.append(
            (retrieval_score, song)
        )

    candidates.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        song
        for _, song in candidates[:limit]
    ]


def score_song(
    user_prefs: Dict,
    song: Dict
) -> Tuple[float, List[str]]:
    """
    Score one song and return evidence explaining the score.
    """

    score = 0.0
    reasons = []

    preferred_genre = (
        user_prefs.get("genre", "")
        .strip()
        .lower()
    )

    preferred_mood = (
        user_prefs.get("mood", "")
        .strip()
        .lower()
    )

    target_energy = float(
        user_prefs.get("energy", 0.5)
    )

    target_tempo = float(
        user_prefs.get("tempo_bpm", 100)
    )

    # Genre
    if (
        preferred_genre
        and song["genre"] == preferred_genre
    ):
        score += 2.0
        reasons.append(
            "genre match (+2.0)"
        )

    # Mood
    if (
        preferred_mood
        and song["mood"] == preferred_mood
    ):
        score += 1.0
        reasons.append(
            "mood match (+1.0)"
        )

    # Energy
    energy_difference = abs(
        song["energy"] - target_energy
    )

    energy_score = (
        max(0.0, 1.0 - energy_difference)
        * 2.0
    )

    score += energy_score

    reasons.append(
        f"energy similarity (+{energy_score:.2f})"
    )

    # Tempo
    tempo_difference = abs(
        song["tempo_bpm"] - target_tempo
    )

    tempo_score = max(
        0.0,
        1.0 - tempo_difference / 100
    )

    score += tempo_score

    reasons.append(
        f"tempo similarity (+{tempo_score:.2f})"
    )

    # Acoustic preference
    if user_prefs.get(
        "likes_acoustic",
        True
    ):
        acoustic_score = song["acousticness"]
    else:
        acoustic_score = (
            1.0 - song["acousticness"]
        )

    score += acoustic_score

    reasons.append(
        f"acoustic preference (+{acoustic_score:.2f})"
    )

    return round(score, 2), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
):
    """
    Retrieve, score, and rank songs.

    This is the single recommendation path
    used by the application.
    """

    candidates = retrieve_candidates(
        user_prefs,
        songs,
        limit=max(k * 2, 10)
    )

    scored = []

    for song in candidates:
        score, reasons = score_song(
            user_prefs,
            song
        )

        scored.append(
            (
                song,
                score,
                ", ".join(reasons)
            )
        )

    scored.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return scored[:k]