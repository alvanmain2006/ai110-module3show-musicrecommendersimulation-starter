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

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

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
- about where bias or unfairness could show up in systems like this



