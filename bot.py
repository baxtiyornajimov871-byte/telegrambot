import os
from flask import Flask, request
import telebot

app = Flask(__name__)

# TOKENNI .env yoki Render Environment Variables dan oladi (xavfsiz!)
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# ====================== WEBHOOK ======================
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    try:
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
    except Exception as e:
        print(e)
    return 'OK', 200

# ====================== BUYRUQLAR ======================
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! 👋\nMen Render.com da 24/7 ishlayapman 🚀")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Hozircha faqat /start va oddiy echo ishlaydi.")

# Oddiy echo (yozgan narsangizni qaytaradi)
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

# ====================== HEALTH CHECK ======================
@app.route('/')
def home():
    return "Telegram Bot Ishlamoqda! ✅"

# ====================== SERVERNI ISHGA TUSHIRISH ======================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
