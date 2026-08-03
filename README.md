
#  Music Recommender Simulation

## Project Summary

This project is a simple content-based music recommendation system built in Python. It compares a user's music preferences with a dataset of 20 songs and ranks the songs based on how well they match.

The recommender uses features such as genre, mood, energy, tempo, and acousticness. Each song receives a score, and the highest-scoring songs are returned as personalized recommendations with explanations showing why they were selected.

---

## How The System Works

Real-world platforms such as Spotify and YouTube use several types of data to recommend music. They may use song features such as genre, mood, tempo, and energy. They also use user behavior such as listening history, likes, skips, searches, and playlists.

Collaborative filtering recommends songs based on the behavior of similar users. Content-based filtering recommends songs whose features are similar to the user's preferences. This project uses a simplified content-based approach.

### Input Data

Each `Song` includes:

* Title
* Artist
* Genre
* Mood
* Energy
* Tempo in BPM
* Valence
* Danceability
* Acousticness

Each user profile includes:

* Preferred genre
* Preferred mood
* Target energy
* Target tempo
* Acoustic preference

### Scoring Rule

The recommender judges every song using the following rules:

* Add `2.0` points for a matching genre.
* Add `1.0` point for a matching mood.
* Add up to `2.0` points based on how close the song's energy is to the user's target energy.
* Add up to `1.0` point based on how close the song's tempo is to the user's target tempo.
* Add up to `1.0` point based on whether the song matches the user's acoustic preference.

The energy score rewards similarity rather than automatically favoring songs with high energy. A song with energy very close to the user's target receives more points than a song with a very different energy value.

### Ranking Rule

The recommender follows this data flow:

```text
User Preferences
       ↓
Score Every Song
       ↓
Store Score and Reasons
       ↓
Sort From Highest to Lowest
       ↓
Return the Top 5 Songs
```

The scoring rule evaluates one song at a time. The ranking rule compares the scores of all songs and selects the strongest matches.

---

## Getting Started

### Setup

1. Create a virtual environment if desired:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt
```

3. Run the app:

```bash
python3 -m src.main
```

### Running Tests

Run the tests with:

```bash
python3 -m pytest
```

Additional tests can be added in `tests/test_recommender.py`.

---

## Sample Recommendation Output

### High-Energy Pop Profile

```text
Profile: High-Energy Pop

1. Sunrise City by Neon Echo
Score: 6.69
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.94), tempo similarity (+0.93), acoustic preference (+0.82)

2. Gym Hero by Max Pulse
Score: 5.72
Because: genre match (+2.0), energy similarity (+1.84), tempo similarity (+0.93), acoustic preference (+0.95)

3. Weekend Motion by City Bloom
Score: 4.67
Because: mood match (+1.0), energy similarity (+1.92), tempo similarity (+0.91), acoustic preference (+0.84)

4. Rooftop Lights by Indigo Parade
Score: 4.46
Because: mood match (+1.0), energy similarity (+1.82), tempo similarity (+0.99), acoustic preference (+0.65)

5. Golden Hour Drive by Sunset Arcade
Score: 4.34
Because: mood match (+1.0), energy similarity (+1.74), tempo similarity (+0.80), acoustic preference (+0.80)
```

### Chill Lofi Profile

```text
Profile: Chill Lofi

1. Library Rain by Paper Lanterns
Score: 6.83
Because: genre match (+2.0), mood match (+1.0), energy similarity (+2.00), tempo similarity (+0.97), acoustic preference (+0.86)

2. Midnight Coding by LoRoom
Score: 6.54
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.86), tempo similarity (+0.97), acoustic preference (+0.71)

3. Cloud Study by Dream Circuit
Score: 5.75
Because: genre match (+2.0), energy similarity (+1.94), tempo similarity (+0.99), acoustic preference (+0.82)

4. Focus Flow by LoRoom
Score: 5.63
Because: genre match (+2.0), energy similarity (+1.90), tempo similarity (+0.95), acoustic preference (+0.78)

5. Spacewalk Thoughts by Orbit Bloom
Score: 4.63
Because: mood match (+1.0), energy similarity (+1.86), tempo similarity (+0.85), acoustic preference (+0.92)
```

### Intense Rock Profile

```text
Profile: Intense Rock

1. Fire Within by Iron Static
Score: 6.85
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.96), tempo similarity (+0.95), acoustic preference (+0.94)

2. Storm Runner by Voltline
Score: 6.79
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.92), tempo similarity (+0.97), acoustic preference (+0.90)

3. Gym Hero by Max Pulse
Score: 4.68
Because: mood match (+1.0), energy similarity (+1.96), tempo similarity (+0.77), acoustic preference (+0.95)

4. Electric Horizon by Nova Rush
Score: 3.67
Because: energy similarity (+1.98), tempo similarity (+0.73), acoustic preference (+0.96)

5. Victory Lap by Street Signal
Score: 3.65
Because: energy similarity (+1.86), tempo similarity (+0.87), acoustic preference (+0.92)
```

---

## Experiments You Tried

I tested the recommender with three different user profiles.

### High-Energy Pop

This profile preferred pop, happy music, high energy, and a tempo near 125 BPM. `Sunrise City` ranked first because it matched both genre and mood while also having energy and tempo values close to the profile.

### Chill Lofi

This profile preferred lofi, chill music, low energy, slower tempos, and acoustic songs. `Library Rain` ranked first because it matched the genre and mood exactly and had an energy value equal to the user's target.

### Intense Rock

This profile preferred rock, intense music, very high energy, and a fast tempo. `Fire Within` ranked first because it matched genre and mood and had energy and tempo values extremely close to the target.

The results changed clearly between profiles. The lofi profile favored slower and more acoustic songs, while the rock profile favored fast and intense songs. The pop profile selected upbeat songs with high danceability and lower acousticness.

### Weight Experiment

I considered reducing the genre weight and increasing the importance of energy. This would allow songs from different genres to rank higher when their energy and tempo strongly match the user's preferences.

However, it could also make the recommendations feel less connected to the user's stated favorite genre. The experiment showed that recommendation quality depends heavily on how the weights are chosen.

---

## Limitations and Risks

This recommender uses a small catalog of only 20 songs, so its recommendations are limited by the available dataset.

The mood and genre labels are manually assigned and may be subjective. Different listeners may describe the same song differently.

The system may create a filter bubble because it rewards songs that closely match preferences the user already provided. This could prevent users from discovering music outside their usual genres or moods.

The system also assumes that all preferences are equally stable. In reality, a user may want calm music while studying and intense music while exercising.

The dataset contains only a small number of songs from each genre, so genres with more songs may have a better chance of appearing in recommendations.

---

## Reflection

This project helped me understand how recommendation systems turn structured data into predictions. The system does not truly understand music. Instead, it compares numerical and categorical features and uses a scoring rule to estimate which songs are most relevant to a user.

One of my biggest learning moments was understanding the difference between scoring and ranking. The scoring function judges one song, while the recommendation function applies that score to the entire catalog and sorts the results.

AI tools helped me design the scoring formulas, organize the code, and debug the imports. However, I still needed to check whether the recommendations made sense and whether the code matched the project requirements. For example, I verified that energy similarity rewarded values closer to the target instead of simply rewarding songs with higher energy.

I was surprised that such a simple weighted system could produce recommendations that felt reasonable. If I continued the project, I would add more songs, learn weights from user feedback, and include collaborative filtering based on users with similar listening behavior.

