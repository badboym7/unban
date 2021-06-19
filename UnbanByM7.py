import telebot
from PIL import Image, ImageFont, ImageDraw
token = input('Token :')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id , "send The name , user and code in this figure\nname:code:user\nEx : \n      Ali Ahmed:12345:@5g77 \nProgrammer : @Z_V_1\n \n \nbot can run in the groups if you want add the bot in your group and when you want make picture send the name,code and user like this:\n \n /make name:code:user\nEx:\n    /make Ali Ahmed:12345:@5g77 \nBy M7 ðŸ‡°ðŸ‡¼")
@bot.message_handler(commands=['make'])
def group(mess):
        try:
                data = mess.text.split("/make")
                data2 = data[1].split(":")
                usr = data2[0]
                pas = data2[1]
                tt = data2[2]
                my_image = Image.open("a2.jpg")
                title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 43)
                title_text = (f'{usr}\n{pas}\n{tt}')
                image_editable = ImageDraw.Draw(my_image)
                image_editable.text((210, 350), title_text, (37, 30, 11), font=title_font)
                my_image.save("ff3gfggf234568.jpg")
                my_image2 = open("ff3gfggf234568.jpg", 'rb')
                bot.send_photo(mess.chat.id, my_image2)
                my_image = Image.open("bp11.jpg")
                title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 78)
                title_text = (f'{usr}\n{pas}\n{tt}')
                image_editable = ImageDraw.Draw(my_image)
                image_editable.text((250, 750), title_text, (37, 30, 20), font=title_font)
                my_image.save("bp1.jpg")
                my_image3 = open("bp1.jpg", 'rb')
                bot.send_photo(mess.chat.id, my_image3)
                my_image = Image.open("bp22.jpg")
                title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 47)
                title_text = (f'{usr}\n{pas}\n{tt}')
                image_editable = ImageDraw.Draw(my_image)
                image_editable.text((250, 430), title_text, (37, 30, 20), font=title_font)
                my_image.save("bp2.jpg")
                my_image4 = open("bp2.jpg", 'rb')
                bot.send_photo(mess.chat.id, my_image4)
        except:
                bot.send_message(mess.chat.id , "send The name , user and code in this figure\nname:code:user\nEx : \n      Ali Ahmed:12345:@5g77 \nProgrammer : @Z_V_1\n \n \nbot can run in the groups if you want add the bot in your group and when you want make picture send the name,code and user like this:\n /make name:code:user\nEx:\n    /make Ali Ahmed:12345:@5g77 \nBy M7 ðŸ‡°ðŸ‡¼")
@bot.message_handler(func=lambda message: True)
def handle_all_message(messagew):
        try:
                if '/make' in messagew.text:
                        data = messagew.text.split("/make")
                        data2 = data[1].split(":")
                        usr = data2[0]
                        pas = data2[1]
                        tt = data2[2]
                        my_image = Image.open("a2.jpg")
                        title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 43)
                        title_text = (f'{usr}\n{pas}\n{tt}')
                        image_editable = ImageDraw.Draw(my_image)
                        image_editable.text((210, 350), title_text, (37, 30, 11), font=title_font)
                        my_image.save("ff3gfggf234568.jpg")
                        my_image2 = open("ff3gfggf234568.jpg", 'rb')
                        bot.send_photo(messagew.chat.id, my_image2)
                        my_image = Image.open("bp11.jpg")
                        title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 78)
                        title_text = (f'{usr}\n{pas}\n{tt}')
                        image_editable = ImageDraw.Draw(my_image)
                        image_editable.text((250, 750), title_text, (37, 30, 20), font=title_font)
                        my_image.save("bp1.jpg")
                        my_image3 = open("bp1.jpg", 'rb')
                        bot.send_photo(messagew.chat.id, my_image3)
                        my_image = Image.open("bp22.jpg")
                        title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 47)
                        title_text = (f'{usr}\n{pas}\n{tt}')
                        image_editable = ImageDraw.Draw(my_image)
                        image_editable.text((250, 430), title_text, (37, 30, 20), font=title_font)
                        my_image.save("bp2.jpg")
                        my_image4 = open("bp2.jpg", 'rb')
                        bot.send_photo(messagew.chat.id, my_image4)
                else:
                        data = messagew.text.split(":")
                        usr = data[0]
                        pas = data[1]
                        tt = data[2]
                        my_image = Image.open("a2.jpg")
                        title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 43)
                        title_text = (f'{usr}\n{pas}\n{tt}')
                        image_editable = ImageDraw.Draw(my_image)
                        image_editable.text((210,350), title_text, (37, 30, 11), font=title_font)
                        my_image.save("ff3gfggf234568.jpg")
                        my_image2 = open("ff3gfggf234568.jpg",'rb')
                        bot.send_photo(messagew.chat.id,my_image2)
                        my_image = Image.open("bp11.jpg")
                        title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 78)
                        title_text = (f'{usr}\n{pas}\n{tt}')
                        image_editable = ImageDraw.Draw(my_image)
                        image_editable.text((250, 750), title_text, (37, 30, 20), font=title_font)
                        my_image.save("bp1.jpg")
                        my_image3 = open("bp1.jpg", 'rb')
                        bot.send_photo(messagew.chat.id, my_image3)
                        my_image = Image.open("bp22.jpg")
                        title_font = ImageFont.truetype('Coming Soon Regular 400.ttf', 47)
                        title_text = (f'{usr}\n{pas}\n{tt}')
                        image_editable = ImageDraw.Draw(my_image)
                        image_editable.text((250, 430), title_text, (37, 30, 20), font=title_font)
                        my_image.save("bp2.jpg")
                        my_image4 = open("bp2.jpg", 'rb')
                        bot.send_photo(messagew.chat.id, my_image4)
        except:
                bot.send_message(messagew.chat.id , "send The name , user and code in this figure\nname:code:user\nEx : \n      Ali Ahmed:12345:@5g77 \nProgrammer : @Z_V_1\n \n \nbot can run in the groups if you want add the bot in your group and when you want make picture send the name,code and user like this:\n /make name:code:user\nEx:\n    /make Ali Ahmed:12344:@5g77 \nBy M7 ðŸ‡°ðŸ‡¼")
bot.polling(True)
 
