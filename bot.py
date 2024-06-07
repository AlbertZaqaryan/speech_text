import telebot
import convert

bot = telebot.TeleBot(token='Your Bot Token')


message_text = convert.text

bot.send_message('Your Bot Chat id', message_text)
