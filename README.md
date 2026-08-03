

# Music Recommender Simulation

## Project Summary

This project is a simple content-based music recommendation system built in Python. It compares a user's music preferences with a catalog of 20 songs and ranks the songs based on how well they match.

The recommender uses features such as genre, mood, energy, tempo, and acousticness. Each song receives a weighted score, and the highest-scoring songs are returned as personalized recommendations with explanations showing why they were selected.

The project also includes input validation and automated tests to verify that invalid preferences are rejected correctly.

---

## How the System Works

Real-world platforms such as Spotify and YouTube use different types of information to recommend music. This can include song features such as genre, mood, tempo, and energy, as well as user behavior such as listening history, likes, skips, searches, and playlists.

Collaborative filtering recommends songs based on the behavior of similar users. Content-based filtering recommends songs whose features are similar to a user's preferences. This project uses a simplified content-based approach.

### Input Data

Each song contains:

- Title
- Artist
- Genre
- Mood
- Energy
- Tempo in BPM
- Valence
- Danceability
- Acousticness

Each user profile contains:

- Preferred genre
- Preferred mood
- Target energy
- Target tempo
- Acoustic preference

---

## Recommendation Process

The system follows this process:

```text
User Preferences
       ↓
Validate Preferences
       ↓
Score Every Song
       ↓
Store Score and Reasons
       ↓
Sort From Highest to Lowest
       ↓
Return the Top 5 Songs
````

### Scoring Rule

The recommender evaluates every song using weighted scoring:

* Add `2.0` points for a matching genre.
* Add `1.0` point for a matching mood.
* Add up to `2.0` points based on energy similarity.
* Add up to `1.0` point based on tempo similarity.
* Add up to `1.0` point based on acoustic preference.

The energy score rewards similarity rather than simply favoring songs with high energy. A song with energy close to the user's target receives more points than a song with a very different energy value.

The same idea is used for tempo, where songs closer to the user's target BPM receive higher scores.

### Ranking

The scoring function evaluates one song at a time. The recommendation function applies the scoring process to the entire catalog, sorts the songs from highest to lowest score, and returns the top five recommendations.

Each recommendation also includes the reasons that contributed to its score.

---

## Input Validation

Before recommendations are generated, user preferences are checked to make sure they are valid.

The validation system checks values such as:

* Energy must be within the supported range.
* Tempo must be between `40` and `220 BPM`.
* The requested genre must exist in the catalog.
* The requested mood must exist in the catalog.

For example, a profile requesting a genre or mood that does not exist in the catalog is rejected instead of producing misleading recommendations.

---

## Project Structure

```text
applied-ai-system-final/
│
├── data/
│   └── songs.csv
│
├── diagrams/
│   └── architecture.mmd
│
├── src/
│   ├── __init__.py
│   ├── logger.py
│   ├── main.py
│   ├── recommender.py
│   └── validation.py
│
├── tests/
│   └── test_recommender.py
│
├── ai_interactions.md
├── model_card.md
├── recommendation_output.txt
├── requirements.txt
└── README.md
```

---

## Getting Started

### Setup

Create a virtual environment if desired:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip3 install -r requirements.txt
```

### Run the Recommender

Run the main program with:

```bash
python3 -m src.main
```

The program loads the song catalog and generates recommendations for the example user profiles.

### Run the Tests

Run the automated tests with:

```bash
python3 -m pytest
```

The final test run passed all 11 tests:

```text
11 passed
```

---

## Sample Recommendation Output

### High-Energy Pop

```text
1. Levitating by Dua Lipa
Score: 6.73
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.96), tempo similarity (+0.78), acoustic preference (+0.99)

2. Watermelon Sugar by Harry Styles
Score: 6.52
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.94), tempo similarity (+0.70), acoustic preference (+0.88)

3. As It Was by Harry Styles
Score: 5.93
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.76), tempo similarity (+0.51), acoustic preference (+0.66)

4. Shape of You by Ed Sheeran
Score: 5.73
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.60), tempo similarity (+0.71), acoustic preference (+0.42)

5. Stay by The Kid LAROI
Score: 5.41
Because: genre match (+2.0), energy similarity (+1.90), tempo similarity (+0.55), acoustic preference (+0.96)
```

### Chill Lofi

The current catalog does not contain the requested `lofi` genre or `chill` mood, so the validation system rejects this profile:

```text
Input validation failed:
- Genre 'lofi' is not in the catalog.
- Mood 'chill' is not in the catalog.
```

This demonstrates that the system validates user preferences before attempting to generate recommendations.

### Intense Rock

```text
1. Smells Like Teen Spirit by Nirvana
Score: 6.54
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.92), tempo similarity (+0.62), acoustic preference (+1.00)

2. Hotel California by Eagles
Score: 5.18
Because: genre match (+2.0), energy similarity (+1.28), tempo similarity (+0.92), acoustic preference (+0.98)

3. Do I Wanna Know? by Arctic Monkeys
Score: 4.59
Because: genre match (+2.0), energy similarity (+1.48), tempo similarity (+0.30), acoustic preference (+0.81)

4. Good 4 U by Olivia Rodrigo
Score: 3.96
Because: mood match (+1.0), energy similarity (+1.42), tempo similarity (+0.88), acoustic preference (+0.66)

5. Can't Hold Us by Macklemore & Ryan Lewis
Score: 3.82
Because: energy similarity (+1.94), tempo similarity (+0.91), acoustic preference (+0.97)
```

---

## Testing and Verification

The project includes automated tests in `tests/test_recommender.py`.

The tests cover:

* Loading the song catalog.
* Correct song data types.
* Recommendation ranking.
* Genre matching.
* Mood matching.
* Energy similarity.
* Tempo similarity.
* Acoustic preference.
* Invalid energy values.
* Invalid tempo values.
* Unknown genres and moods.

The final test result was:

```text
11 passed in 0.03s
```

The recommendation program was also executed separately to verify that the system produces ranked recommendations and displays validation errors when a profile contains unsupported preferences.

---

## Weight Experiment

I considered reducing the genre weight and increasing the importance of energy. This would allow songs from different genres to rank higher when their energy and tempo strongly match the user's preferences.

However, reducing the genre weight could make recommendations feel less connected to the user's stated favorite genre.

This experiment showed that recommendation quality depends heavily on how the scoring weights are chosen. The weights determine which features have the greatest influence on the final ranking.

---

## Limitations and Risks

This recommender uses a small catalog of only 20 songs, so its recommendations are limited by the available dataset.

The mood and genre labels are manually assigned and may be subjective. Different listeners may describe the same song differently.

The system may create a filter bubble because it rewards songs that closely match preferences the user already provided. This could prevent users from discovering music outside their usual genres or moods.

The system also assumes that preferences remain stable. In reality, a user may want calm music while studying and intense music while exercising.

The dataset contains only a small number of songs from each genre, so genres with more songs may have a better chance of appearing in recommendations.

The system is also not a production recommendation engine. It does not use listening history, collaborative filtering, user feedback, or a learned machine learning model.

---

## Reflection

This project helped me understand how recommendation systems turn structured data into predictions. The system does not truly understand music. Instead, it compares numerical and categorical features and uses a scoring rule to estimate which songs are most relevant to a user.

One of my biggest learning moments was understanding the difference between scoring and ranking. The scoring function judges one song, while the recommendation function applies that score to the entire catalog and sorts the results.

AI tools helped me design the scoring formulas, organize the code, and debug the imports. However, I still needed to check whether the recommendations made sense and whether the code matched the project requirements.

For example, I verified that energy similarity rewards values closer to the target instead of simply rewarding songs with higher energy. I also tested invalid preferences to make sure the validation system rejected unsupported energy, tempo, genre, and mood values.

I was surprised that such a simple weighted system could produce recommendations that felt reasonable. If I continued the project, I would add more songs, learn weights from user feedback, and include collaborative filtering based on users with similar listening behavior.

````

