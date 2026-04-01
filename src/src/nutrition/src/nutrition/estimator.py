from .usda import get_protein

PROTEIN_KEYWORDS = [
    "paneer", "tofu", "soya", "chana",
    "rajma", "dal", "lentil", "curd",
    "yogurt", "sprouts"
]

def estimate(text: str, usda_key: str) -> float:
    total = 0.0
    text = (text or "").lower()

    for item in PROTEIN_KEYWORDS:
        if item in text:
            total += get_protein(usda_key, item)

    return round(total, 1)
``
