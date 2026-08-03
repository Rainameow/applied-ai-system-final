from src.recommender import load_songs, recommend_songs
from src.validation import validate_preferences


def get_user_preferences():
    print("\nMusic Recommender")
    print("=" * 40)

    genre = input(
        "What genre do you want? "
    ).strip().lower()

    mood = input(
        "What mood do you want? "
    ).strip().lower()

    while True:
        try:
            energy = float(
                input("Energy level (0.0 - 1.0): ")
            )

            if 0.0 <= energy <= 1.0:
                break

            print("Please enter a value between 0.0 and 1.0.")

        except ValueError:
            print("Please enter a number.")

    while True:
        try:
            tempo = float(
                input("Target tempo in BPM (40 - 220): ")
            )

            if 40 <= tempo <= 220:
                break

            print("Please enter a tempo between 40 and 220.")

        except ValueError:
            print("Please enter a number.")

    while True:
        acoustic = input(
            "Do you like acoustic songs? (yes/no): "
        ).strip().lower()

        if acoustic in ["yes", "y"]:
            likes_acoustic = True
            break

        if acoustic in ["no", "n"]:
            likes_acoustic = False
            break

        print("Please enter yes or no.")

    return {
        "genre": genre,
        "mood": mood,
        "energy": energy,
        "tempo_bpm": tempo,
        "likes_acoustic": likes_acoustic,
    }


def main():
    songs = load_songs("data/songs.csv")

    print(f"\nLoaded songs: {len(songs)}")

    user_prefs = get_user_preferences()

    errors = validate_preferences(
        user_prefs,
        songs
    )

    if errors:
        print("\nInput validation failed:")
        for error in errors:
            print(f"- {error}")
        return

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5
    )

    print("\n" + "=" * 60)
    print("YOUR RECOMMENDATIONS")
    print("=" * 60)

    for i, (song, score, reasons) in enumerate(
        recommendations,
        start=1
    ):
        print(
            f"\n{i}. {song['title']} "
            f"by {song['artist']}"
        )
        print(f"Score: {score}")
        print(f"Because: {reasons}")


if __name__ == "__main__":
    main()