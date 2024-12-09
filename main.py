import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

jokes = [
    "Почему программисты не могут попасть в рай? Потому что они всегда ищут баги.",
    "Как программисты перезагружают свои мозги? Они говорят: 'sudo reboot'.",
    "Почему компьютер не может плавать? Потому что он не любит водяных знаков!"
]

async def start(update: Update, context):
    await update.message.reply_text("Привет! Напиши мне 'шутка', и я расскажу тебе смешную шутку!")

async def random_joke(update: Update, context):
    joke = random.choice(jokes)
    await update.message.reply_text(joke)

if __name__ == "__main__":
    TELEGRAM_TOKEN = "8168233263:AAHcWtO3fwmTb-vnvOy_fmusMWivXqdA93c"
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, random_joke))
    print("Бот запущен!")
    app.run_polling()
