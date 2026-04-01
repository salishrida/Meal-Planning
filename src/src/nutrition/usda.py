import requests

def get_protein(api_key: str, ingredient: str) -> float:
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {"api_key": api_key}
    body = {"query": ingredient, "pageSize": 1}

    r = requests.post(url, params=params, json=body).json()
    foods = r.get("foods", [])

    if not foods:
        return 0.0

    for n in foods[0].get("foodNutrients", []):
        if n["nutrientName"].lower() == "protein":
            return float(n["value"])
    return 0.0
