import requests
import telebot
bot_token = "6491509221:AAFAYAAeYG1pIgRnNKQsKweitMOGPNLRb_I"
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "قم بارسال يوزر الانستقرام")
@bot.message_handler(func=lambda message: True)
def send_image(message):
    username = message.text
    url = "https://instagram130.p.rapidapi.com/account-info"
    querystring = {"username": username}
    headers = {
        "X-RapidAPI-Key": "bae7fb229cmsha9bea2816dbfab6p10f014jsnb0542ff1f583",
        "X-RapidAPI-Host": "instagram130.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if 'profile_pic_url' in data:
        profile_pic_url = data['profile_pic_url']
        chat_id = message.chat.id
        bot.send_photo(chat_id, profile_pic_url)
    else:
        bot.reply_to(message, "لا يوجد مستخدم يحمل هذا اليوزر")

bot.polling()
