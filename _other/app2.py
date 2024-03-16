import time

import telebot
import config
from chemlib import Compound

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['get_molar_mass'])
def get_molar_mass(message, substance):
    compound = Compound(substance)
    print('%.0f' % compound.molar_mass())


def get_mass_fraction(substance, atom):
    compound = Compound(substance)
    print('%.0f' % compound.percentage_by_mass(atom) + '%')


if __name__ == '__main__':
    print('----------------Bot start-----------------\n')
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(3)