"""
Music Recommender Simulation

A content-based music recommendation system
with retrieval, transparent scoring, validation,
and reliability testing.
"""

from src.recommender import (
    load_songs,
    recommend_songs
)

from src.validation import (
    validate_preferences
)


USER_PROFILES = {

    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "tempo_bpm": 125,
        "likes_acoustic": False,
    },

    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "tempo_bpm": 75,
        "likes_acoustic": True,
    },

    "Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "tempo_bpm": 155,
        "likes_acoustic": False,
    },
}


def display_recommendations(
    profile_name: str,
    user_prefs: dict,
    songs: list
) -> None:
    """Display recommendations for one profile."""

    errors = validate_preferences(
        user_prefs,
        songs
    )

    if errors:

        print(
            f"\nProfile: {profile_name}"
        )

        print(
            "Input validation failed:"
        )

        for error in errors:
            print(
                f"- {error}"
            )

        return

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5
    )

    print(
        "\n"
        + "=" * 65
    )

    print(
        f"Profile: {profile_name}"
    )

    print(
        "=" * 65
    )

    for number, (
        song,
        score,
        explanation
    ) in enumerate(
        recommendations,
        start=1
    ):

        print(
            f"\n{number}. "
            f"{song['title']} "
            f"by {song['artist']}"
        )

        print(
            f"Score: {score:.2f}"
        )

        print(
            f"Because: {explanation}"
        )


def main() -> None:
    """Load the catalog and test profiles."""

    songs = load_songs(
        "data/songs.csv"
    )

    print(
        f"Loaded songs: {len(songs)}"
    )

    print(
        "\nMusic Recommender Simulation"
    )

    print(
        "Retrieval + weighted scoring + validation"
    )

    for (
        profile_name,
        user_prefs
    ) in USER_PROFILES.items():

        display_recommendations(
            profile_name,
            user_prefs,
            songs
        )


if __name__ == "__main__":
    main()