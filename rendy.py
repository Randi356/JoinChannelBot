import os
import telebot

# my telegram org by rendy 
API_KEY = os.getenv('API_KEY')
bot = telebot.Telebot(API_KEY)

# chatbot commad by rendy
bot.message_handler(commad=['gay'])
def gay(message):
  bot.reply_to(message, "hallo gay")
  
# running
bot.polling()
  
