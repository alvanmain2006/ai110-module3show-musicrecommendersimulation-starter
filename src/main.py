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


    # Starter example profile
    user_prefs = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.85,
    "target_tempo_bpm": 125,
    "target_valence": 0.80,
    "target_danceability": 0.82,
    "target_acousticness": 0.20
}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n🎵 Top Song Recommendations 🎵\n")

    for i, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"{i}. 🎶 {song['title']} - {song['artist']}")
        print(f"   ⭐ Score: {score:.2f}/10")
        print(f"   🎼 Genre: {song['genre']}")
        print(f"   😊 Mood : {song['mood']}")
        print(f"   💡 Reason(s): {reasons}")
        print("=" * 60)


if __name__ == "__main__":
    main()
