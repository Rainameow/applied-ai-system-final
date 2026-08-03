# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Intended Use

VibeMatch is a content-based music recommendation system that recommends songs based on a user's stated music preferences.

The system considers preferences such as genre, mood, energy level, tempo, and acoustic preference. It is designed primarily as a classroom and portfolio project to demonstrate how a recommendation system can use structured data, weighted scoring, validation, and explanations.

The system assumes that a user's stated preferences are a reasonable representation of the type of music they currently want to hear. It does not learn from a user's actual listening history, likes, skips, or playlists.

---

## 3. How the Model Works

VibeMatch uses a content-based recommendation approach. Instead of learning from other users, it compares the characteristics of each song with the preferences provided by the user.

Each song contains several features:

- Genre
- Mood
- Energy
- Tempo in BPM
- Valence
- Danceability
- Acousticness

The user provides:

- Preferred genre
- Preferred mood
- Target energy
- Target tempo
- Acoustic preference

Each song receives a weighted compatibility score.

The scoring system:

- Matching genre adds 2 points.
- Matching mood adds 1 point.
- Energy similarity contributes up to 2 points.
- Tempo similarity contributes up to 1 point.
- Acoustic preference contributes up to 1 point.

Songs are then sorted by their total scores, and the five highest-scoring songs are returned.

The system also provides an explanation for each recommendation, showing which features contributed to the score.

Compared with the original starter logic, the final system adds tempo similarity, preference validation, error handling, explanations, and automated tests. The system also checks that user preferences contain valid energy and tempo values and that the requested genre and mood exist in the catalog.

---

## 4. Data

The recommender uses a catalog of **20 real songs**.

The catalog contains songs from several genres, including:

- Pop
- Rock
- Acoustic
- Indie
- Hip-hop

The songs also represent different moods, including:

- Happy
- Energetic
- Intense
- Relaxed
- Sad
- Moody
- Romantic

Each song is represented using structured features such as energy, tempo, valence, danceability, and acousticness.

The catalog is intentionally small because this is an educational project. It does not represent the full range of available music.

Important aspects of musical taste are missing, including:

- Listening history
- Favorite artists
- Lyrics
- Personal associations with songs
- User ratings
- Skips
- Playlists
- Time of day
- Activity or context
- Individual user behavior

Because of this, the recommendations should be viewed as a demonstration of recommendation logic rather than a production music recommendation system.

---

## 5. Strengths

The system works well when a user's preferences are clearly represented by the features in the catalog.

For example, a user who prefers high-energy pop can receive songs that match their preferred genre while also being close to their target energy and tempo.

The weighted scoring system also allows different preferences to affect the final ranking instead of relying on only one feature.

Another strength is that the system explains its recommendations. Instead of only returning a song title, it shows reasons such as:

- Genre match
- Mood match
- Energy similarity
- Tempo similarity
- Acoustic preference

The validation system is another strength. Invalid energy values, invalid tempo values, and preferences that do not exist in the catalog are rejected rather than silently producing potentially misleading recommendations.

---

## 6. Limitations and Bias

The system has several important limitations.

First, the catalog contains only 20 songs. This means that recommendations are limited to the available songs and may not represent a user's actual musical interests.

The system also relies heavily on manually assigned categories such as genre and mood. Musical mood can be subjective, so different listeners may classify the same song differently.

The scoring system can also favor songs that match the user's stated preferences too closely. This may reduce musical discovery and create a simple form of a filter bubble.

Some genres and moods have more representation in the catalog than others. This can affect which types of songs appear in the recommendations.

The system also does not use listening behavior. A user may say they like a particular genre but rarely listen to it in practice. The recommender cannot detect this difference.

Finally, the feature weights were designed for this project rather than learned from a large collection of user feedback. Therefore, the weights may not represent how real users would value each feature.

---

## 7. Evaluation

The recommender was evaluated using multiple user profiles representing different music preferences.

The tested profiles included:

- **High-Energy Pop**
- **Chill Lofi**
- **Intense Rock**

The recommendations were checked to make sure songs with matching genres, moods, energy levels, tempos, and acoustic preferences received appropriate scores.

Automated tests were also created for the recommendation system.

The final test suite contains **11 tests**, and all 11 tests passed.

The tests check functionality including:

- Loading the music catalog
- Recommendation ranking
- Recommendation explanations
- Energy scoring
- Tempo scoring
- Genre matching
- Mood matching
- Invalid energy rejection
- Invalid tempo rejection
- Unknown genre rejection
- Unknown mood rejection

The evaluation showed that the recommender can produce different results for different user profiles and that invalid preferences are handled safely.

---

## 8. Future Work

There are several ways the system could be improved.

### Larger Dataset

The catalog could be expanded from 20 songs to thousands of songs to provide more useful recommendations and better genre diversity.

### User Feedback

The system could learn from likes, dislikes, skips, and ratings instead of relying only on manually entered preferences.

### Collaborative Filtering

A future version could recommend songs based on users with similar listening behavior.

### Better Personalization

The system could consider different contexts, such as:

- Studying
- Working out
- Driving
- Relaxing
- Sleeping

### Recommendation Diversity

The recommender could intentionally include some songs that are slightly outside the user's normal preferences to encourage music discovery.

### Better Evaluation

A larger evaluation dataset with real user feedback could be used to measure recommendation accuracy and user satisfaction.

---

## 9. Personal Reflection

This project helped me understand how recommendation systems can turn structured information into personalized results.

One of the most important things I learned was the difference between scoring and ranking. The scoring system evaluates how well an individual song matches a user's preferences, while the ranking system compares all of the songs and selects the highest-scoring ones.

I also learned that a recommendation system does not necessarily need a complicated machine learning model to produce understandable results. A weighted scoring system can already create reasonable recommendations when the input features are meaningful.

An unexpected part of the project was seeing how much the final recommendations can change when the scoring weights or user preferences change.

This project also made me think more critically about the limitations of recommendation systems. A system can appear personalized while still being limited by its dataset, feature choices, and assumptions about what a user likes.

If I continued developing VibeMatch, I would add a larger dataset, real user feedback, and methods for recommending new music while still maintaining transparency about why each song was selected.