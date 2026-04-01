import os
from dotenv import load_dotenv

load_dotenv()

def env(key, default=None):
    return os.getenv(key, default)

YOUTUBE_API_KEY = env("YOUTUBE_API_KEY")
USDA_API_KEY = env("USDA_API_KEY")

EMAIL_FROM = env("EMAIL_FROM")
EMAIL_TO = env("EMAIL_TO")
SMTP_HOST = env("SMTP_HOST")
SMTP_PORT = int(env("SMTP_PORT", "587"))
SMTP_USER = env("SMTP_USER")
SMTP_PASS = env("SMTP_PASS")

KEYWORDS = env("KEYWORDS", "").split(",")
MIN_PROTEIN_G = float(env("MIN_PROTEIN_G", "15"))
TOP_N = int(env("TOP_N", "5"))
