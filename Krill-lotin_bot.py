from transliterate import to_cyrillic, to_latin
import telebot
import re

Token = "7995149683:AAG4335-ZU0w_42_8eKVIGV0UoGWVicPiLk"
bot = telebot.TeleBot(Token, parse_mode=None)

def detect_lang(text):
    # Maxsus belgilarni tozalaymiz
    text = re.sub(r"[^\w\s]", "", text)
    text = text.replace('\u200b', '').replace('\xa0', '').strip()
    latin_count = sum(ch.lower() in 'abcdefghijklmnopqrstuvwxyz' for ch in text)
    cyrillic_count = sum('а' <= ch.lower() <= 'я' or ch.lower() in 'ёғқҳў' for ch in text)
    return 'latin' if latin_count >= cyrillic_count else 'cyrillic'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text.strip()
    lang = detect_lang(msg)

    if lang == "latin":
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)

    bot.reply_to(message, javob)  

bot.infinity_polling()
