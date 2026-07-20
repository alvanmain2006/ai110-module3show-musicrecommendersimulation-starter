# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
Music Finder
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  
Intended for all music lovers
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Takes in a user's preference about the type of genre, mood, and target numerical data to evaluate a score for a song then recommend it based on its score.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains 20 songs.
It includes genres such as Pop, Rock, Hip-Hop, EDM, Lofi, Jazz, Classical, Country, R&B, and Indie.
It also includes moods like Happy, Calm, Energetic, Sad, Romantic, and Relaxed.
I added 10 additional songs to increase the variety of genres and moods.
The dataset is still limited and does not include every music genre or enough songs to represent all musical tastes.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  
The system works well for users with clear preferences, such as High-Energy Pop or Chill Lofi listeners.
The scoring correctly rewards songs that closely match the user's genre, mood, energy, and tempo.
The recommendations generally matched my expectations, with energetic profiles receiving upbeat songs and relaxed profiles receiving slower, more acoustic songs.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- The system works for a lot of general profiles, but if a profile is more niche, the system might give a "hail mary" type of result. I think it is not that the system has biases, but rather that our data are not big enough. I also think with more data from the user's preference, we could more likely to capture more accurate results. With more data, naturally come with more changes to how we evaluate the system's feature, like which one weight more or less.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

High-Energy Pop vs. Chill Lofi

The recommendations were very different between these two profiles. The High-Energy Pop profile mainly recommended fast, energetic songs with high danceability, while the Chill Lofi profile recommended slower and more acoustic songs. This makes sense because the user preferences for energy, tempo, and acousticness were almost opposite, so the scoring algorithm naturally favored different songs.

High-Energy Pop vs. Impossible Profile

The High-Energy Pop profile produced recommendations with higher scores because many songs in the dataset matched its preferences. The Impossible Profile received lower scores since it combined features that rarely exist together. Even so, the recommender still returned the songs that were the closest overall matches instead of failing completely.

Chill Lofi vs. Impossible Profile

The Chill Lofi profile consistently recommended calm, low-energy songs that matched the user's desired vibe. The Impossible Profile produced more varied recommendations because no single song satisfied all of its preferences. Instead, the recommender selected songs that matched a few important characteristics while sacrificing others.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Some extra data for the user's preference would definitely help a lot more with the accuracy of the system.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

The experiment was fun to do, because I had to find all kind of scores and genre to make the most unique types of profile. I think this project really give me a good idea of how music and potentially movie recommender works. I think I learn a lot from this project, not only about machine learning but also coding practices in general.