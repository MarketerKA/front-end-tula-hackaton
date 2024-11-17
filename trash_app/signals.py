from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=Bid)
# def notify_user_on_bid_status_change(sender, instance, **kwargs):
#     if instance.status == 'accepted':
#         print(f'Notify {instance.user.username}: Your bid for {instance.trash_can} has been accepted.')
#     elif instance.status == 'rejected':
#         print(f'Notify {instance.user.username}: Your bid for {instance.trash_can} has been rejected.')


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bid
from telegram import Bot
import os
from dotenv import load_dotenv
# Load the Telegram bot token from environment variables

load_dotenv(".env")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)

@receiver(post_save, sender=Bid)
def notify_user_on_completion(sender, instance, **kwargs):
    # Check if the bid status is 'completed'
    if instance.status == 'completed':
        # Find the Telegram user associated with this bid
        bot.send_message(
            chat_id=instance.username,
            text=f"Здравствуйте! Ваша заявка #{instance.id} завершена. Спасибо за ваше обращение!"
        )

def notify_user(bid: Bid):
    bot.send_message(
        chat_id=bid.chat_id,
        text=f"Ваша заявка: {bid.type} по улице: {bid.coordinates} была завершена. Спасибо за ваше обращение!"
    )