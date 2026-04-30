import os
from flask import Flask, request
import telebot

app = Flask(__name__)

# Tokenni to'g'ridan kodga yozdik (test uchun)
TOKEN = "8612921933:AAFHHytczKklS-Qtua_zrUF9mZsmZMk2jYM"
bot = telebot.TeleBot(TOKEN)

print("🚀 Bot ishga tushdi!")

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    try:
        update = telebot.types.Update.de_json(request.get_data().decode('utf-8'))
        bot.process_new_updates([update])
        print("✅ Xabar qabul qilindi!")
    except Exception as e:
        print("❌ XATO:", str(e))
    return 'OK', 200

# Oddiy buyruqlar
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Salom! Bot nihoyat ishlayapti! 🎉")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Hozircha faqat /start ishlaydi")

# Har qanday xabarga javob
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Siz yozdingiz: " + message.text)

@app.route('/')
def home():
    return "Bot ishlamoqda! ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
