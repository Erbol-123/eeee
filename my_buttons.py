from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)



main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

about = KeyboardButton(text='About')
main_menu.add(KeyboardButton('Videosabaqlar'),
              KeyboardButton('Uy jumislari'),
              KeyboardButton('Kursqa jaziliw'))        
              

   

about_menu = InlineKeyboardMarkup()
admin = InlineKeyboardButton(text='Admin',
                             url='https://t.me/mtkrvd')
youtube = InlineKeyboardButton(text='Instagram',
                               url='https://www.youtube.com')

about_menu.add(admin,youtube)