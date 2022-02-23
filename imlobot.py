import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWords import checkWords
from transliterate import to_latin,to_cyrillic

API_TOKEN = "5286814898:AAGMtZqoDNNZiCarnc5nMafMPbu2GodEFo8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    await message.reply("Imlo botimizga Xush kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message ):
    await message.reply("So'z yuboring!")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = to_cyrillic(message.text)
    result = checkWords(word)
    if result['available']:
        word = to_latin(word)
        response = f"+ {word.capitalize()}"
    else:
        word = to_latin(word)
        response = f"x {word.capitalize()}\n"
        for text in result["matches"]:
            text = to_latin(text)
            response += f"+ {text.capitalize()}\n"
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)