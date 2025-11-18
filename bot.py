import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = os.getenv("BOT_TOKEN")



TOKEN = os.getenv("8087967837:AAFMohxcGiuqgTOEEWU8NY0MDJaF5j3ywzI")
GROUP_ID = -1003325165006

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Flask dummy server
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask).start()

# FORM HOLATI
class Form(StatesGroup):
    fio = State()
    phone = State()
    video = State()

@dp.message(Command("start"))
async def start_cmd(message: types.Message, state: FSMContext):
    await message.answer("Salom! F.I.O kiriting:")
    await state.set_state(Form.fio)

@dp.message(Form.fio)
async def get_fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(Form.phone)

@dp.message(Form.phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Endi videoni yuboring:")
    await state.set_state(Form.video)

@dp.message(Form.video, F.video)
async def get_video(message: types.Message, state: FSMContext):
    data = await state.get_data()
    fio = data["fio"]
    phone = data["phone"]
    file_id = message.video.file_id

    caption = f"📌 Yangi ishtirokchi!\n👤 FIO: {fio}\n📞 Telefon: {phone}"

    await bot.send_video(chat_id=GROUP_ID, video=file_id, caption=caption)
    await message.answer("Video qabul qilindi! Rahmat!")
    await state.clear()

async def main():
    await dp.start_polling(bot)

asyncio.run(main())


