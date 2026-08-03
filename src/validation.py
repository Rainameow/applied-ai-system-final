def validate_preferences(user_prefs: dict, songs: list = None) -> list:
    """Validate user preferences and return a list of errors."""

    errors = []

    # Make sure preferences are a dictionary
    if not isinstance(user_prefs, dict):
        return ["Preferences must be provided as a dictionary."]

    # Check required fields
    required_fields = ["genre", "mood", "energy"]

    for field in required_fields:
        if field not in user_prefs:
            errors.append(f"Missing required preference: {field}")

    # Stop here if required fields are missing
    if errors:
        return errors

    genre = user_prefs["genre"]
    mood = user_prefs["mood"]

    # Validate genre
    if not isinstance(genre, str) or not genre.strip():
        errors.append("Genre cannot be empty.")

    # Validate mood
    if not isinstance(mood, str) or not mood.strip():
        errors.append("Mood cannot be empty.")

    # Validate energy
    try:
        energy = float(user_prefs["energy"])

        if not 0 <= energy <= 1:
            errors.append("Energy must be between 0 and 1.")

    except (TypeError, ValueError):
        errors.append("Energy must be a number.")

    # Validate tempo
    if "tempo_bpm" in user_prefs:
        try:
            tempo = float(user_prefs["tempo_bpm"])

            if tempo < 40 or tempo > 220:
                errors.append(
                    "Tempo must be between 40 and 220 BPM."
                )

        except (TypeError, ValueError):
            errors.append("Tempo must be a number.")

    # Validate acoustic preference
    if "likes_acoustic" in user_prefs:
        if not isinstance(user_prefs["likes_acoustic"], bool):
            errors.append(
                "likes_acoustic must be True or False."
            )

    # Check genre against the actual music catalog
    if songs is not None and isinstance(genre, str):
        available_genres = {
            song["genre"].lower()
            for song in songs
            if "genre" in song
        }

        if genre.lower() not in available_genres:
            errors.append(
                f"Genre '{genre}' is not in the catalog."
            )

    # Check mood against the actual music catalog
    if songs is not None and isinstance(mood, str):
        available_moods = {
            song["mood"].lower()
            for song in songs
            if "mood" in song
        }

        if mood.lower() not in available_moods:
            errors.append(
                f"Mood '{mood}' is not in the catalog."
            )

    return errors