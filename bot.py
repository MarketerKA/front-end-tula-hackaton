import os
import django
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
# Set the environment variable and initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trash_project.settings')  # Replace 'your_project' with your project name
django.setup()

from trash_app.models import Bid  # Replace 'app' with your app name
from trash_app.bids.views import create_bid
from django.contrib.auth.models import User
load_dotenv(".env")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    await update.message.reply_text(
        "Привет! Я помогу вам оформить заявку. Отправьте фотографию с описанием и адресом через запятую.\n"
        "Пример: \nОписание: Свалка возле дома.\nАдрес: Улица Пушкина, дом Колотушкина."
    )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photo messages with description and address."""
    user = update.message.chat
    photo = update.message.photo[-1]  # Get the highest quality photo
    file_id = photo.file_id
    # Parse caption
    caption = update.message.caption or ""
    if "," not in caption:
        await update.message.reply_text(
            "Пожалуйста, отправьте описание и адрес через запятую.\nПример: Описание: Свалка возле дома, Адрес: Улица Пушкина, дом Колотушкина."
        )
        return

    # Split the caption into description and address
    try:
        description, address = map(str.strip, caption.split(",", 1))
    except ValueError:
        await update.message.reply_text("Не удалось разобрать описание и адрес. Пожалуйста, проверьте формат.")
        return

    # Download photo
    file = await context.bot.get_file(file_id)
    file_path = f"media/trash_cans/{file_id}.jpg"
    await file.download_to_drive(file_path)

    await sync_to_async(Bid.objects.create)(
        username=update.effective_user.username,
        chat_id=update.message.chat_id,
        type="trash",
        image=file_path,
        description=description,
        coordinates=address,
        status="pending",
    )

    await update.message.reply_text(
        f"Спасибо! Ваша заявка принята.\nОписание: {description}\nАдрес: {address}"
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages."""
    await update.message.reply_text("Пожалуйста, отправьте фотографию с описанием и адресом.")


def main():
    # Create the application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Start the bot
    application.run_polling()


if __name__ == "__main__":
    main()
