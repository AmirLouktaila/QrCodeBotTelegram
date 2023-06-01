import telebot
import qrcode
import random
import cv2
from pyzbar.pyzbar import decode
bot = telebot.TeleBot("5860213339:AAEaz5qVv8YBmbe-TBzV41ceNUAp2NGYoao")
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

@bot.message_handler(content_types=['photo'])
def photo(message):
    print ('message.photo ='), message.photo
    fileID = message.photo[-1].file_id
    print ('fileID ='), fileID
    file_info = bot.get_file(fileID)
    print ('file.file_path ='), file_info.file_path
    downloaded_file = bot.download_file(file_info.file_path)
    names_code="photo"+str(a)+".png"
    with open(names_code, 'wb') as new_file:
        new_file.write(downloaded_file)
    img=cv2.imread(names_code)
    for code in decode(img):
        bot.reply_to(message,code.data.decode('utf-8'))



bot.infinity_polling()
