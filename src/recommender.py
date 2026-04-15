from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
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
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []
        
        for song in self.songs:
            score = 0
            
            if song.genre == user.favorite_genre:
                score += 3
            
            if song.mood == user.favorite_mood:
                score += 2
            
            score += (10 - abs(song.energy - user.target_energy))
            
            if user.likes_acoustic:
                score += song.acousticness
            
            scored.append((song, score))
        
        scored.sort(key=lambda x: x[1], reverse=True)
        
        return [s[0] for s in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        
        if song.genre == user.favorite_genre:
            reasons.append("matches your favorite genre")
        
        if song.mood == user.favorite_mood:
            reasons.append("matches your mood")
        
        if abs(song.energy - user.target_energy) < 2:
            reasons.append("similar energy level")
        
        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("acoustic style")
        
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    import csv
    
    songs = []
    
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append(row)
    
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0
    reasons = []
    
    if song["genre"] == user_prefs["genre"]:
        score += 3
        reasons.append("genre match")
    
    if song["mood"] == user_prefs["mood"]:
        score += 2
        reasons.append("mood match")
    
    energy_diff = abs(float(song["energy"]) - user_prefs["energy"])
    score += (10 - energy_diff)
    reasons.append("energy similarity")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    results = []
    
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        results.append((song, score, explanation))
    
    results.sort(key=lambda x: x[1], reverse=True)
    
    return results[:k]