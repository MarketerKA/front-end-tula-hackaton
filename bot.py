from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)
from asgiref.sync import sync_to_async
import os
import django
from dotenv import load_dotenv

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trash_project.settings')  # Replace 'trash_project' with your project name
django.setup()
load_dotenv(".env")

from trash_app.models import Bid
from trash_app.image_classifier import predict_image, CLASSES

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Conversation states
ASK_IMAGE, ASK_DESCRIPTION, ASK_ADDRESS = range(3)

# Temporary storage for user data in memory
user_data = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Initiate the conversation."""
    await update.message.reply_text("Привет! Я помогу вам оформить заявку. Отправьте фотографию свалки.")
    return ASK_IMAGE


async def ask_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photo and ask for description."""
    photo = update.message.photo[-1]  # Get the highest quality photo
    file = await context.bot.get_file(photo.file_id)
    file_path = f"media/trash_cans/{photo.file_id}.jpg"
    await file.download_to_drive(file_path)

    # Store image path in user data
    context.user_data['image'] = file_path

    await update.message.reply_text("Фото сохранено! Теперь напишите описание проблемы.")
    return ASK_DESCRIPTION


async def ask_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle description and ask for address."""
    description = update.message.text
    context.user_data['description'] = description

    await update.message.reply_text("Спасибо! Теперь отправьте адрес.")
    return ASK_ADDRESS


async def save_bid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle address and save the bid."""
    address = update.message.text
    context.user_data['address'] = address

    if predict_image(context.user_data['image']) in CLASSES:
        await update.message.reply_text(
            f"Подождите Искусственный интеллект проверяет вашу фотографию",
            reply_markup=ReplyKeyboardRemove()
        )
        pass

    await sync_to_async(Bid.objects.create)(
        username=update.effective_user.username,
        chat_id=update.message.chat_id,
        type="trash",
        image=context.user_data['image'],
        description=context.user_data['description'],
        coordinates=context.user_data['address'],
        status="pending",
    )

    await update.message.reply_text(
        f"Спасибо! Ваша заявка принята.\nОписание: {context.user_data['description']}\nАдрес: {context.user_data['address']}",
        reply_markup=ReplyKeyboardRemove()
    )


    # Clear user data after submission
    context.user_data.clear()

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the conversation."""
    await update.message.reply_text("Операция отменена.", reply_markup=ReplyKeyboardRemove())
    context.user_data.clear()
    return ConversationHandler.END


def main():
    # Create the application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Define conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_IMAGE: [MessageHandler(filters.PHOTO, ask_description)],
            ASK_DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_address)],
            ASK_ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_bid)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Add conversation handler to the application
    application.add_handler(conv_handler)

    # Start the bot
    application.run_polling()


if __name__ == "__main__":
    main()
