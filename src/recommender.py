from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_tempo: float
    target_valence: float
    target_danceability: float
    target_acousticness: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:

            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)
    print(f"Loading songs from {csv_path}...")
    return songs
    
    

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns:
        (score, reasons)
    """

    score = 0.0
    reasons = []

    # Genre (2.5 points)
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 2.5
        reasons.append("Genre matched")

    # Mood (1.5 points)
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.5
        reasons.append("Mood matched")

    # Tempo (up to 2 points)
    tempo_diff = abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"])

    if tempo_diff <= 5:
        score += 2.0
        reasons.append("Very similar tempo")
    elif tempo_diff <= 15:
        score += 1.5
        reasons.append("Similar tempo")
    elif tempo_diff <= 30:
        score += 1.0
        reasons.append("Somewhat similar tempo")

    # Energy (up to 1.5 points)
    energy_diff = abs(song["energy"] - user_prefs["target_energy"])

    if energy_diff <= 0.10:
        score += 1.5
        reasons.append("Very similar energy")
    elif energy_diff <= 0.25:
        score += 1.0
        reasons.append("Similar energy")

    # Danceability (up to 1 point)
    dance_diff = abs(song["danceability"] - user_prefs["target_danceability"])

    if dance_diff <= 0.10:
        score += 1.0
        reasons.append("Danceability matched")
    elif dance_diff <= 0.20:
        score += 0.5

    # Valence (up to 1 point)
    valence_diff = abs(song["valence"] - user_prefs["target_valence"])

    if valence_diff <= 0.10:
        score += 1.0
        reasons.append("Similar positivity")
    elif valence_diff <= 0.20:
        score += 0.5

    # Acousticness (up to 0.5 point)
    acoustic_diff = abs(song["acousticness"] - user_prefs["target_acousticness"])

    if acoustic_diff <= 0.10:
        score += 0.5
        reasons.append("Acousticness matched")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    recommendations = []

    for song in songs:

        score, reasons = score_song(user_prefs, song)

        recommendations.append(
            (
                song,
                score,
                ", ".join(reasons)
            )
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:k]