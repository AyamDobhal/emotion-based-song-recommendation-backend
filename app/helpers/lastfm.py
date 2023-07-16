from random import sample
from typing import Any, List

import requests


def get_artwork(artist: str, song: str) -> str:
    """
    Get artwork from iTunes API
    """
    term = f"{'+'.join(artist.split())}+{'+'.join(song.split())}"
    req = requests.get(
        f"https://itunes.apple.com/search?term={term}&entity=song&limit=1&attribute=artistTerm"
    )
    data = req.json()
    if len(data["results"]) == 0:
        return "https://i.imgur.com/kzNpjvh.png"
    return data["results"][0]["artworkUrl100"]


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
            "image_url": get_artwork(song["artist"]["name"], song["name"]),
        }
        for song in data
    ]
