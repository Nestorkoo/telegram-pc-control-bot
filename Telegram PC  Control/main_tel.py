

import sqlite3
import os
from sound import Sound
from keyboard import Keyboard
import telebot
import time
import webbrowser
import threading
from telebot import types



TOKEN = '6586371091:AAHTMlmL3dDrUt1Ft2ikW2y7k9hONzUaMxI'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome_screen(message):
    bot.send_message(message.chat.id, 'Hello!')
    handle_system_functions(message)

def handle_system_functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    volume_btn = types.KeyboardButton('System Functions ⚙️')
    app_btn = types.KeyboardButton('Apps Control 🖥️')
    markup.add(volume_btn, app_btn)
    bot.send_message(message.chat.id, 'Select the functions: ', reply_markup=markup)

#     SYSTEM BUTTONS    ##
def handle_volume_control(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    volume_up = types.KeyboardButton('+2 🔊')
    volume_down = types.KeyboardButton('-2 🔉')
    max_volume = types.KeyboardButton('100% 🔊')
    min_volume = types.KeyboardButton('0% 🔇')
    hulf_volume = types.KeyboardButton('50% 🔉')
    ten_volume = types.KeyboardButton('10% 🔉')
    custom_volume = types.KeyboardButton('Custom Volume 🔊')
    back_btn = types.KeyboardButton('🔙')
    markup.add(volume_up, volume_down, max_volume, min_volume, hulf_volume, ten_volume, custom_volume, back_btn)
    bot.send_message(message.chat.id, 'Select the functions for control audio', reply_markup=markup)

##  END SYSTEM BUTTONS  ##



## APPS CONTROL ##

def handle_apps_control(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    calc_btn = types.KeyboardButton('Open Calculator 🔢')
    YouTube = types.KeyboardButton('Open YouTube 📽️')
    Chrome = types.KeyboardButton('Open Chrome 🌐')
    explorer = types.KeyboardButton('Open Explorer 📂')
    
    
    

    back = types.KeyboardButton('🔙')
    markup.add(calc_btn, YouTube, Chrome, explorer,back)
    bot.send_message(message.chat.id, 'Select the functions: ', reply_markup=markup)


## END APPS CONTROL ##

@bot.message_handler(content_types='text')
def handle_text(message):
    if message.text == 'System Functions ⚙️':
        handle_volume_control(message)
    elif message.text == 'Apps Control 🖥️':
        handle_apps_control(message)
    elif message.text == 'Open Explorer 📂':
        os.startfile('Explorer')
    elif message.text == 'Open Calculator 🔢':
        os.startfile('calc.exe')
    elif message.text == 'Open Chrome 🌐':
        os.startfile('Chrome')
    elif message.text == 'Open YouTube 📽️':
        webbrowser.open_new('https://www.youtube.com/')
    
    elif message.text == '🔙':
        handle_system_functions(message)
    elif message.text == '+2 🔊':
        Sound.volume_up()
    elif message.text == '-2 🔉':
        Sound.volume_down()
    elif message.text == '100% 🔊':
        Sound.volume_max()
    elif message.text == '0% 🔇':
        Sound.volume_min()
    elif message.text == '50% 🔉':
        Sound.volume_set(50)
    elif message.text == '10% 🔉':
        Sound.volume_set(10)
    elif message.text == 'Custom Volume 🔊':
        msg = bot.send_message(message.chat.id, 'Write the volume which you want 😊')
        bot.register_next_step_handler(msg, handle_custom_volume)




    

    


def handle_custom_volume(message):
    try:
        user_volume = int(message.text)
        Sound.volume_set(user_volume)
        handle_system_functions(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Try again')
        handle_text(message)
    ################################################################

    
    
    


    
bot.polling(none_stop=True)


# bot_thread = threading.Thread(target=bot_polling)
# bot_thread.start()


