import requests

from random import sample
from typing import List, Any

def get_song(emotion: str, api_key: str) -> str:
    """
    Get song from LastFM API
    """
    url = "https://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "tag.gettoptracks",
        "tag": emotion,
        "api_key": api_key,
        "format": "json",
        "limit": 100,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return serialize_song_data(sample(data["tracks"]["track"], 10))

def serialize_song_data(data: List[Any]):
    """
    Serialize song data
    """
    return [
        {
            "name": song["name"],
            "artist": song["artist"]["name"],
            "url": song["url"],
            "image_url": song["image"][2]["#text"]
        }
        for song in data
    ]