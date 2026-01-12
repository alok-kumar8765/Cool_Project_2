import smtplib, requests
from email.mime.text import MIMEText

from config import EMAIL_CONFIG, TELEGRAM_CONFIG


def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_CONFIG["email"]
    msg["To"] = EMAIL_CONFIG["to"]

    server = smtplib.SMTP(EMAIL_CONFIG["smtp"], EMAIL_CONFIG["port"])
    server.starttls()
    server.login(EMAIL_CONFIG["email"], EMAIL_CONFIG["password"])
    server.send_message(msg)
    server.quit()


def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_CONFIG['bot_token']}/sendMessage"
    requests.post(url, data={
        "chat_id": TELEGRAM_CONFIG["chat_id"],
        "text": text
    })


def notify(subject, message):
    if EMAIL_CONFIG["enabled"]:
        send_email(subject, message)

    if TELEGRAM_CONFIG["enabled"]:
        send_telegram(f"{subject}\n\n{message}")
