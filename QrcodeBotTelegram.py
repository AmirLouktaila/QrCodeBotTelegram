import telebot
import qrcode
import random
import requests
bot = telebot.TeleBot("YourTokenBot")
a=random.randint(1000,10000000)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.reply_to(message, text='Hello in Quick response image generator')
@bot.message_handler(func=lambda m: True)
def echo_all(m):
    cid=m.chat.id
    img = qrcode.make(m.text)
    names="photo"+str(a)+".png"
    type(img)
    img.save(names)
    photo = open(f"C:\\Users\\Admin\\Desktop\\pylkt\\{names}",'rb')
    bot.send_photo(m.chat.id,photo)
    photo.close()









bot.infinity_polling()
