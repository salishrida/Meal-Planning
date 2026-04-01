import smtplib
from email.mime.text import MIMEText

def send_email(cfg, recipes):
    body = ""
    for r in recipes:
        body += f"{r.title}\n{r.url}\nProtein: {r.protein_g} g\n\n"

    msg = MIMEText(body)
    msg["Subject"] = "🍽️ Meal‑Planning: High‑Protein Veg Recipes"
    msg["From"] = cfg.EMAIL_FROM
    msg["To"] = cfg.EMAIL_TO

    with smtplib.SMTP(cfg.SMTP_HOST, cfg.SMTP_PORT) as s:
        s.starttls()
        s.login(cfg.SMTP_USER, cfg.SMTP_PASS)
        s.send_message(msg)
