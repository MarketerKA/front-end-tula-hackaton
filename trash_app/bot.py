import os
from telegram import Bot, Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from django.core.wsgi import get_wsgi_application

# Django интеграция
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trash_app.settings')  # Замените на ваше имя проекта
# application = get_wsgi_application()

from models import Bid  # Импортируйте вашу модель Bid
from django.contrib.auth.models import User

# Загрузите токен из .env или переменной окружения
TELEGRAM_BOT_TOKEN = '7694280802:AAG9qOO8uoYwYlpuDHZ0x89ZEnLn7fMIAik'

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Я помогу вам оформить заявку на устранение свалки. "
        "Отправьте фотографию и опишите проблему."
    )

# Обработка фото
def handle_photo(update: Update, context: CallbackContext):
    user = update.message.chat
    photo = update.message.photo[-1]  # Берем фото наивысшего качества
    file_id = photo.file_id
    caption = update.message.caption or "Без описания"

    # Скачиваем фото
    file = context.bot.get_file(file_id)
    file_path = f"media/trash_cans/{file_id}.jpg"
    file.download(file_path)

    # Сохраняем заявку в базе данных
    user_instance, created = User.objects.get_or_create(username=f"tg_{user.id}")
    bid = Bid.objects.create(
        user=user_instance,
        type="trash",
        image=file_path,
        description=caption,
        status="pending",
    )

    update.message.reply_text(
        f"Спасибо! Ваша заявка #{bid.id} принята. Мы скоро свяжемся с вами."
    )

# Обработка текстовых сообщений
def handle_text(update: Update, context: CallbackContext):
    update.message.reply_text("Пожалуйста, отправьте фотографию для оформления заявки.")

# Основной блок
def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Команды
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработчики сообщений
    dispatcher.add_handler(MessageHandler(filters.photo, handle_photo))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_text))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
