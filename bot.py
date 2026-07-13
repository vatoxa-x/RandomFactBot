import telebot
from config import token
from logic import get_fact,speak
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def bot_start(message):
    bot.reply_to(
        message,
        f"Привет, {message.from_user.first_name}!\n"
        "Я бот который может рассказать интересные факты\n"
        "Напиши /fact чтобы получить факт",)
@bot.message_handler(commands = ['fact'])
def bot_fact(message):
    fact = get_fact()
    bot.reply_to(message, fact)
    speak(fact)
if __name__ == "__main__":
    bot.infinity_polling()
    