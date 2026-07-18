# 🎵 Music Recommender Simulation

## Project Summary


This project is a simple music recommender system built in Python. It reads song data from a CSV file, compares each song to a user's preferences, and recommends the songs with the highest scores. The recommendations are based on genre, mood, and energy, and each recommendation includes an explanation of why it was selected.

---

## How The System Works


The recommender uses three main song features:

- Genre
- Mood
- Energy

The user profile stores the user's favorite genre, favorite mood, and preferred energy level.

Each song is compared to the user's preferences. A genre match earns 2 points, a mood match earns 1 point, and songs with energy levels close to the user's target receive additional similarity points.

After every song is scored, the songs are sorted from highest to lowest score, and the top five songs are recommended along with a short explanation showing why they matched.

Data Flow:

User Preferences → Compare with Every Song → Calculate Score → Sort Songs → Return Top Recommendations
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

C:\Users\nagee\ai110-module3show-musicrecommendersimulation-starter>python -m pytest
================================ test session starts ============================================
platform win32 -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\nagee\ai110-module3show-musicrecommendersimulation-starter
plugins: anyio-4.13.0
collected 2 items                                                                                                               

tests\test_recommender.py ..                                                                                              [100%]

================================== 2 passed in 0.12s ============================================


```

---

## Sample Recommendation Output

========== Gym Lover ==========

Gym Hero - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

Sunrise City - Score: 2.87
Because: genre match (+2.0), energy similarity (+0.87)

Golden Weekend - Score: 2.79
Because: genre match (+2.0), energy similarity (+0.79)

Fire Within - Score: 1.99
Because: mood match (+1.0), energy similarity (+0.99)

Storm Runner - Score: 1.96
Because: mood match (+1.0), energy similarity (+0.96)


========== Study Mode ==========

Focus Flow - Score: 4.00
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.00)

Deep Focus - Score: 3.93
Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.93)

Midnight Coding - Score: 2.98
Because: genre match (+2.0), energy similarity (+0.98)

Library Rain - Score: 2.95
Because: genre match (+2.0), energy similarity (+0.95)

Coffee Shop Stories - Score: 0.97
Because: energy similarity (+0.97)


---

## Experiments You Tried


I tested the recommender using three different user profiles:

- Gym Lover
- Study Mode
- Relaxing Evening

Each profile produced different recommendations based on its preferences. The Gym Lover profile recommended energetic pop songs, the Study Mode profile recommended focused lofi songs, and the Relaxing Evening profile recommended relaxing jazz songs.

I also expanded the dataset by adding eight new songs with different genres and moods. This gave the recommender more variety when generating recommendations.


---

## Limitations and Risks


This recommender only uses genre, mood, and energy to make recommendations. It does not consider listening history, favorite artists, lyrics, or user ratings.

The dataset is also very small, so some genres and moods have fewer songs than others. Because genre has the highest weight in the scoring system, songs with matching genres are often ranked higher than songs with similar moods or energy levels.

---


## Reflection

This project helped me understand how recommendation systems convert user preferences into predictions using simple scoring rules. Even without machine learning, the recommender was able to produce reasonable song suggestions by comparing song features with user preferences.

I also learned that recommendation systems can have bias. If the dataset is small or the scoring gives too much importance to one feature, some songs or genres may be recommended more often than others. Testing multiple user profiles showed how changing user preferences changes the recommendations.



