from src.recommender import (
    load_songs,
    score_song,
    recommend_songs
)

from src.validation import validate_preferences


def sample_song():
    return {
        "id": 1,
        "title": "Test Pop Track",
        "artist": "Test Artist",
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "tempo_bpm": 120,
        "valence": 0.9,
        "danceability": 0.8,
        "acousticness": 0.2,
    }


def test_catalog_loads():
    songs = load_songs("data/songs.csv")

    assert len(songs) == 20
    assert songs[0]["title"] == "Blinding Lights"


def test_genre_match_adds_two_points():
    score, reasons = score_song(
        {
            "genre": "pop",
            "mood": "",
            "energy": 0.5,
            "tempo_bpm": 100,
            "likes_acoustic": False,
        },
        sample_song()
    )

    assert "genre match (+2.0)" in reasons
    assert score > 2.0


def test_mood_match_adds_one_point():
    score, reasons = score_song(
        {
            "genre": "",
            "mood": "happy",
            "energy": 0.5,
            "tempo_bpm": 100,
            "likes_acoustic": False,
        },
        sample_song()
    )

    assert "mood match (+1.0)" in reasons
    assert score > 1.0


def test_exact_energy_scores_higher():
    exact, _ = score_song(
        {
            "genre": "",
            "mood": "",
            "energy": 0.8,
            "tempo_bpm": 100,
            "likes_acoustic": False,
        },
        sample_song()
    )

    distant, _ = score_song(
        {
            "genre": "",
            "mood": "",
            "energy": 0.2,
            "tempo_bpm": 100,
            "likes_acoustic": False,
        },
        sample_song()
    )

    assert exact > distant


def test_exact_tempo_scores_higher():
    exact, _ = score_song(
        {
            "genre": "",
            "mood": "",
            "energy": 0.5,
            "tempo_bpm": 120,
            "likes_acoustic": False,
        },
        sample_song()
    )

    distant, _ = score_song(
        {
            "genre": "",
            "mood": "",
            "energy": 0.5,
            "tempo_bpm": 180,
            "likes_acoustic": False,
        },
        sample_song()
    )

    assert exact > distant


def test_recommendations_are_sorted():
    songs = load_songs("data/songs.csv")

    results = recommend_songs(
        {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "tempo_bpm": 125,
            "likes_acoustic": False,
        },
        songs,
        k=5
    )

    assert len(results) == 5

    for i in range(4):
        assert results[i][1] >= results[i + 1][1]


def test_invalid_energy_is_rejected():
    songs = load_songs("data/songs.csv")

    errors = validate_preferences(
        {
            "genre": "pop",
            "mood": "happy",
            "energy": 2.0,
            "tempo_bpm": 125,
            "likes_acoustic": False,
        },
        songs
    )

    assert any(
        "Energy must be between 0 and 1"
        in error
        for error in errors
    )


def test_invalid_tempo_is_rejected():
    songs = load_songs("data/songs.csv")

    errors = validate_preferences(
        {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 300,
            "likes_acoustic": False,
        },
        songs
    )

    assert any(
        "Tempo must be between 40 and 220 BPM"
        in error
        for error in errors
    )


def test_unknown_genre_is_rejected():
    songs = load_songs("data/songs.csv")

    errors = validate_preferences(
        {
            "genre": "afrobeats",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "likes_acoustic": False,
        },
        songs
    )

    assert any(
        "not in the catalog"
        in error
        for error in errors
    )


def test_unknown_mood_is_rejected():
    songs = load_songs("data/songs.csv")

    errors = validate_preferences(
        {
            "genre": "pop",
            "mood": "sleepy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "likes_acoustic": False,
        },
        songs
    )

    assert any(
        "not in the catalog"
        in error
        for error in errors
    )


def test_returns_requested_number_of_recommendations():
    songs = load_songs("data/songs.csv")

    results = recommend_songs(
        {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "tempo_bpm": 75,
            "likes_acoustic": True,
        },
        songs,
        k=3
    )

    assert len(results) == 3