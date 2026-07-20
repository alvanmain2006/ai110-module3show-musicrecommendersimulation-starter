# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

So my version of a recommender system, would first let user pick a bunch of song that they like, then average out the data of the song, then I will use that data as the preference to compare to other new songs. I will calculate the difference between the preference and the new songs, then applied the weight for each difference score of a song. My version will prioritize a song's tempo, so it will have more of a weight compare to other features. Once all the songs are computed, we rank them based on the score they get, and recommend the most similar song.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
User Preferences
                      │
                      ▼
        Load songs from songs.csv
                      │
                      ▼
      Loop through every song in the dataset
                      │
                      ▼
        Compare song features with user profile
                      │
                      ▼
        Calculate weighted similarity score
                      │
                      ▼
        Save (song, score, explanation)
                      │
                      ▼
      Sort songs by score (highest first)
                      │
                      ▼
          Return Top 5 Recommendations

          Algorithm Recipe
Load every song from the CSV file.
Create a user preference profile containing genre, mood, tempo, energy, valence, danceability, and acousticness.
Compare every song to the user profile.
Award weighted points based on feature similarity:
Genre match: +2.5
Mood match: +1.5
Tempo similarity: up to +2.0
Energy similarity: up to +1.5
Danceability similarity: up to +1.0
Valence similarity: up to +1.0
Acousticness similarity: up to +0.5
Calculate a total score for each song.
Rank all songs by score and return the top k recommendations along with an explanation of why each song was selected.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

🎵 Top Song Recommendations 🎵

1. 🎶 Sunrise City - Neon Echo
   ⭐ Score: 9.50/10
   🎼 Genre: pop
   😊 Mood : happy
   💡 Reason(s): Genre matched, Mood matched, Similar tempo, Very similar energy, Danceability matched, Similar positivity, Acousticness matched
============================================================

2. 

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

Model 1:
high_energy_pop = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.90,
    "target_tempo_bpm": 130,
    "target_valence": 0.85,
    "target_danceability": 0.90,
    "target_acousticness": 0.15
}
Result:
1. 🎶 Sunrise City - Neon Echo
   ⭐ Score: 9.00/10
   🎼 Genre: pop
   😊 Mood : happy
   💡 Reason(s): Genre matched, Mood matched, Similar tempo, Very similar energy, Similar positivity, Acousticness matched
============================================================
2. 🎶 Gym Hero - Max Pulse
   ⭐ Score: 8.50/10
   🎼 Genre: pop
   😊 Mood : intense
   💡 Reason(s): Genre matched, Very similar tempo, Very similar energy, Danceability matched, Similar positivity, Acousticness matched
============================================================
3. 🎶 Rooftop Lights - Indigo Parade
   ⭐ Score: 6.00/10
   🎼 Genre: indie pop
   😊 Mood : happy
   💡 Reason(s): Mood matched, Similar tempo, Similar energy, Danceability matched, Similar positivity
============================================================
4. 🎶 Electric Bloom - Aurora X
   ⭐ Score: 5.50/10
   🎼 Genre: EDM
   😊 Mood : Energetic
   💡 Reason(s): Very similar tempo, Very similar energy, Danceability matched, Similar positivity
============================================================
5. 🎶 City Lights - Nova Skyline
   ⭐ Score: 5.00/10
   🎼 Genre: Synthpop
   😊 Mood : Upbeat
   💡 Reason(s): Similar tempo, Similar energy, Danceability matched, Similar positivity, Acousticness matched
=========================================


Model 2:
chill_lofi = {
    "favorite_genre": "lofi",
    "favorite_mood": "calm",
    "target_energy": 0.30,
    "target_tempo_bpm": 75,
    "target_valence": 0.50,
    "target_danceability": 0.40,
    "target_acousticness": 0.85
}

Result:
1. 🎶 Library Rain - Paper Lanterns
   ⭐ Score: 8.00/10
   🎼 Genre: lofi
   😊 Mood : chill
   💡 Reason(s): Genre matched, Very similar tempo, Very similar energy, Similar positivity, Acousticness matched
============================================================
2. 🎶 Focus Flow - LoRoom
   ⭐ Score: 7.50/10
   🎼 Genre: lofi
   😊 Mood : focused
   💡 Reason(s): Genre matched, Very similar tempo, Similar energy, Similar positivity, Acousticness matched
============================================================
3. 🎶 Midnight Coding - LoRoom
   ⭐ Score: 6.50/10
   🎼 Genre: lofi
   😊 Mood : chill
   💡 Reason(s): Genre matched, Very similar tempo, Similar energy, Similar positivity
============================================================
4. 🎶 Ocean Drift - Blue Horizon
   ⭐ Score: 6.50/10
   🎼 Genre: Ambient
   😊 Mood : Calm
   💡 Reason(s): Mood matched, Similar tempo, Very similar energy, Similar positivity, Acousticness matched
============================================================
5. 🎶 Spacewalk Thoughts - Orbit Bloom
   ⭐ Score: 5.00/10
   🎼 Genre: ambient
   😊 Mood : chill
   💡 Reason(s): Similar tempo, Very similar energy, Danceability matched, Acousticness matched
============================================================


Model 3:
impossible_profile = {
    "favorite_genre": "classical",
    "favorite_mood": "energetic",
    "target_energy": 1.00,
    "target_tempo_bpm": 220,
    "target_valence": 1.00,
    "target_danceability": 1.00,
    "target_acousticness": 1.00
}

Result:
1. 🎶 Electric Bloom - Aurora X
   ⭐ Score: 5.00/10
   🎼 Genre: EDM
   😊 Mood : Energetic
   💡 Reason(s): Mood matched, Very similar energy, Danceability matched, Similar positivity
============================================================
2. 🎶 Moon Waltz - Silver Quartet
   ⭐ Score: 3.00/10
   🎼 Genre: Classical
   😊 Mood : Peaceful
   💡 Reason(s): Genre matched, Acousticness matched
============================================================
3. 🎶 Gym Hero - Max Pulse
   ⭐ Score: 2.00/10
   🎼 Genre: pop
   😊 Mood : intense
   💡 Reason(s): Very similar energy
============================================================
4. 🎶 Rooftop Lights - Indigo Parade
   ⭐ Score: 2.00/10
   🎼 Genre: indie pop
   😊 Mood : happy
   💡 Reason(s): Similar energy
============================================================
5. 🎶 City Lights - Nova Skyline
   ⭐ Score: 2.00/10
   🎼 Genre: Synthpop
   😊 Mood : Upbeat
   💡 Reason(s): Similar energy
============================================================
---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions

I learned a lot of about recommendation systems, and machine learning in this lesson. I think I will be able to applied these learning concepts into my personal coding projects.



