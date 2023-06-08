import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import random

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with buttons when the /start command is issued."""
    reply_markup = ReplyKeyboardMarkup([[KeyboardButton('/baha')]])
    await update.message.reply_text("Привет! Я бот Баха. Нажми кнопку /baha.", reply_markup=reply_markup)


async def baha_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random response when the /baha command is issued."""
    if should_ignore_message():
        return

    responses = ["Эмне", "А", "Чё там"]
    response = random.choice(responses)
    user_id = str(update.effective_user.id)
    if user_id == "508794153":
        response += " Аччкощщник"
    elif user_id == "842359304":
        response += " Рина младший"
    elif user_id == "427927690":
        response += "Иринат"
    await update.message.reply_text(response)


async def ignore_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ignore the message with a chance of 60%."""
    if should_ignore_message():
        return
    # Don't send any reply when ignoring the message


def should_ignore_message() -> bool:
    """Check if a message should be ignored based on a 60% chance."""
    return random.random() < 0.7


def main() -> None:
    application = Application.builder().token("5632323063:AAGQAScEihkWERze46FuT4vc8-4bNtI58hk").build()

    application.add_handler(CommandHandler("start", start_command, filters=filters.COMMAND))
    application.add_handler(CommandHandler("baha", baha_command, filters=filters.COMMAND))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ignore_message))

    application.run_polling()


if __name__ == "__main__":
    main()
