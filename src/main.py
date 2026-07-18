"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "Gym Lover": {
            "genre": "pop",
            "mood": "intense",
            "energy": 0.95
        },
        "Study Mode": {
            "genre": "lofi",
            "mood": "focused",
            "energy": 0.40
        },
        "Relaxing Evening": {
            "genre": "jazz",
            "mood": "relaxed",
            "energy": 0.30
        }
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n========== {profile_name} ==========\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()