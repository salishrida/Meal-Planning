import config
from sources.youtube import fetch_youtube
from nutrition.estimator import estimate
from ranker import rank
from emailer import send_email

def run():
    recipes = []

    for q in config.KEYWORDS:
        recipes.extend(fetch_youtube(config.YOUTUBE_API_KEY, q))

    for r in recipes:
        r.protein_g = estimate(r.description, config.USDA_API_KEY)

    top = rank(recipes, config.MIN_PROTEIN_G, config.TOP_N)
    send_email(config, top)

if __name__ == "__main__":
    run()
