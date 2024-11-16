import requests

from django.conf import settings

def send_telegram_message(username, message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': f"@{username}",  # Use @username to send the message
        'text': message,
    }
    response = requests.post(url, data=payload)
    return response.json()