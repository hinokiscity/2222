import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.utils.token import TokenValidationError
import asyncio


# ==== TOKENNI ENV'DAN OLAMIZ ====
TOKEN = os.getenv("BOT_TOKEN")

if TOKEN is None:
    raise TokenValidationError("BOT_TOKEN environment variable topilmadi!")

# ==== BOT VA DISPATCHER ====
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


# ==== START COMMAND ====
@dp.message(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Bot ishlayapti! 🚀\nXush kelibsiz!")


# ==== ECHO HANDLER ====
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


# ==== BOTNI ISHGA TUSHIRISH ====
async def main():
    print("Bot ishga tushdi... 🚀")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
