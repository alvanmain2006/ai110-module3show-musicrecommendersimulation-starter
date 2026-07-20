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
    impossible_profile = {
    "favorite_genre": "classical",
    "favorite_mood": "energetic",
    "target_energy": 1.00,
    "target_tempo_bpm": 220,
    "target_valence": 1.00,
    "target_danceability": 1.00,
    "target_acousticness": 1.00
}

    recommendations = recommend_songs(impossible_profile, songs, k=5)

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
