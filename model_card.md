# 🎧 Model Card: Music Recommender Simulation


## 1. Model Name

MusicMatch 1.0

---

## 2. Intended Use  


This recommender is designed to suggest songs based on a user's music preferences. It compares the user's favorite genre, mood, and energy level with the songs in the dataset and recommends the best matches.

The model assumes the user knows what genre, mood, and energy level they prefer.

This project is for classroom learning to demonstrate how a simple recommendation system works, not for real-world music streaming services.


---

## 3. How the Model Works  


The recommender uses three song features: genre, mood, and energy.

It compares these features with the user's preferences. A matching genre earns 2 points, a matching mood earns 1 point, and songs with energy levels close to the user's target receive additional similarity points.

After every song is scored, the songs are sorted from highest to lowest score, and the top recommendations are returned with an explanation of why they were selected.


Compared to the starter code, I implemented the main recommendation logic. I added code to load songs from the CSV file, score each song based on genre, mood, and energy, sort the songs by their scores, and return the top recommendations. I also added explanations showing why each song was recommended.



---

## 4. Data  


The dataset contains 18 songs after adding 8 new songs.

It includes different genres such as pop, rock, lofi, jazz, ambient, indie pop, folk, and EDM. It also includes different moods like happy, chill, focused, relaxed, intense, peaceful, and moody.

Although the dataset is more diverse after expansion, it is still very small and cannot represent all music styles or user preferences.


---

## 5. Strengths  


The recommender works well when users have clear preferences for genre, mood, and energy.

During testing, the recommendations matched my expectations. For example, the Gym Lover profile recommended energetic pop songs, while the Study Mode profile recommended calm lofi songs. The Relaxing Evening profile recommended jazz and relaxing music.

---

## 6. Limitations and Bias 


The recommender only considers genre, mood, and energy. It ignores other useful features such as artist, tempo, danceability, listening history, and personal favorites.

The scoring system also gives a large reward for matching genres, which can cause songs from other genres with similar moods or energy levels to rank lower.

Because the dataset is small, some genres and moods are represented more than others, which can affect the recommendations.



---

## 7. Evaluation  


I tested the recommender using three different user profiles:

- Gym Lover
- Study Mode
- Relaxing Evening

The recommendations changed based on each profile's preferences.

Gym Lover recommended energetic pop songs such as Gym Hero.

Study Mode recommended focused lofi songs such as Focus Flow.

Relaxing Evening recommended relaxing jazz songs such as Evening Café.

These results showed that the recommender responded correctly to different user preferences.





---

## 8. Future Work  

If I continued developing this project, I would:

- Add a much larger music dataset.
- Include more song features such as artist, tempo, and danceability.
- Learn from a user's listening history instead of only using manually entered preferences.
- Recommend a wider variety of songs instead of focusing mostly on exact genre matches.

 

---

## 9. Personal Reflection  


This project helped me understand how recommendation systems work using simple scoring rules instead of complex AI models.

I was surprised that a few simple rules could produce recommendations that felt reasonable.

Using AI helped me understand the coding process, but I still tested my program and made sure I understood how each function worked before using the results.


