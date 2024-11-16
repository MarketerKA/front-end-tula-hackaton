import os
import django
from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Подключение Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from models import Bid, User

BOT_TOKEN = "YOUR_BOT_TOKEN"

# Этапы диалога
DESCRIPTION, PHOTO, ADDRESS = range(3)

# Начало диалога
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Добро пожаловать! Опишите проблему, например: 'Переполненный контейнер'."
    )
    return DESCRIPTION

# Шаг 1: Получение описания проблемы
def handle_description(update: Update, context: CallbackContext):
    context.user_data['description'] = update.message.text
    update.message.reply_text(
        "Отлично! Теперь отправьте фото проблемы."
    )
    return PHOTO

# Шаг 2: Получение фото
def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]  # Выбираем фото с наибольшим разрешением
    file = context.bot.get_file(photo.file_id)
    file_path = f"media/trash_cans/{photo.file_id}.jpg"
    file.download(file_path)

    context.user_data['photo_path'] = f"trash_cans/{photo.file_id}.jpg"

    update.message.reply_text(
        "Фото получено! Теперь отправьте адрес, где находится проблема."
    )
    return ADDRESS

# Шаг 3: Получение адреса
def handle_address(update: Update, context: CallbackContext):
    address = update.message.text
    context.user_data['address'] = address

    # Сохраняем пользователя в базе данных или получаем существующего
    user = update.message.from_user
    telegram_user, created = User.objects.get_or_create(
        username=user.username,
        defaults={'role': 'citizen'}
    )

    # Создаем запись заявки в базе данных
    Bid.objects.create(
        user=telegram_user,
        type='trash',
        address=context.user_data['address'],
        image=context.user_data['photo_path'],
        description=context.user_data['description'],
    )

    update.message.reply_text(
        "Спасибо! Ваша заявка зарегистрирована. Мы свяжемся с вами после ее обработки.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

# Отмена диалога
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Вы отменили отправку заявки. Если хотите начать заново, используйте /start.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

# Настройка обработчиков
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Определяем диалог
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            DESCRIPTION: [MessageHandler(Filters.text & ~Filters.command, handle_description)],
            PHOTO: [MessageHandler(Filters.photo, handle_photo)],
            ADDRESS: [MessageHandler(Filters.text & ~Filters.command, handle_address)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
