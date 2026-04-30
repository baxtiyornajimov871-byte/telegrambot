import os
from flask import Flask, request
import telebot

app = Flask(__name__)

# =================== TOKEN (VAQTINCHA TO'G'RIDAN YOZAMIZ) ===================
TOKEN = "8612921933:AAFHHytczKklS-Qtua_zrUF9mZsmZMk2jYM"
bot = telebot.TeleBot(TOKEN)

print("✅ Bot ishga tushdi! Token kod ichida.")

# ====================== WEBHOOK ======================
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    try:
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        print("✅ Update qabul qilindi!")
    except Exception as e:
        print("❌ XATO:", str(e))
    return 'OK', 200

# ====================== BUYRUQLAR ======================
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Salom! Bot muvaffaqiyatli ishlamoqda! 🚀")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Yordam: /start")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

@app.route('/')
def home():
    return "Telegram Bot Ishlamoqda! ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
