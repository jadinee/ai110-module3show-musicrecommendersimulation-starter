"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("---- Stress Test ----\n")

    user1 = {"genre": "pop", "mood": "happy", "energy": 0.9}
    user2 = {"genre": "lofi", "mood": "calm", "energy": 0.2}
    user3 = {"genre": "rock", "mood": "sad", "energy": 0.9}

    for i, user in enumerate([user1, user2, user3], start=1):
        print(f"User {i}: {user}")
        recs = recommend_songs(user, songs, k=5)
        
        for song, score, explanation in recs:
            print(f"{song['title']} - {score:.2f}")
        
        print()


if __name__ == "__main__":
    main()
