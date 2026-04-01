import requests
from typing import List
from ..models import Recipe

def fetch_youtube(api_key: str, query: str) -> List[Recipe]:
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 5,
        "key": api_key
    }

    res = requests.get(url, params=params).json()
    recipes = []

    for item in res.get("items", []):
        vid = item["id"]["videoId"]
        snip = item["snippet"]
        recipes.append(
            Recipe(
                title=snip["title"],
                url=f"https://www.youtube.com/watch?v={vid}",
                source="YouTube",
                description=snip.get("description", "")
            )
        )
    return recipes
