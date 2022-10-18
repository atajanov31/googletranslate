import logging
from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from button import menu
from states import Translate
from googletrans import Translator

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊\nTarjima turini tanlang", reply_markup=menu)
    await Translate.lang.set()


@dp.message_handler(state=Translate.lang)
async def which_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data(
        {"lang": lang},
    )
    await message.answer(f"Tarjima qilinuvchi matnni kiriting")
    #await Translate.next()
    await Translate.trans.set()

@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    lang = data.get("lang")
    tarjimon = Translator()
    if lang == "🇺🇿 Uzb - 🇬🇧 Eng":
        tarjima = tarjimon.translate(text, dest="de")
        await message.answer(tarjima.text, reply_markup=menu)
    elif lang == "🇬🇧 Eng - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=menu)
    # elif lang == "🇺🇿 Uzb - 🇷🇺 Rus":
    #     tarjima = tarjimon.translate(text, dest="ru")
    #     await message.answer(tarjima.text, reply_markup=menu)
    # elif lang == "🇷🇺 Rus - 🇺🇿 Uzb":
    #     tarjima = tarjimon.translate(text, dest="uz")
    #     await message.answer(tarjima.text, reply_markup=menu)
    # elif lang == "🇺🇿 Uzb - fr French":
    #     tarjima = tarjimon.translate(text, dest="fr")
    #     await message.answer(tarjima.text, reply_markup=menu)
    # elif lang == "fr French - 🇺🇿 Uzb":
    #     tarjima = tarjimon.translate(text, dest="uz")
    #     await message.answer(tarjima.text, reply_markup=menu)
    elif lang == "🇺🇿 Uzb - de German ":
        tarjima = tarjimon.translate(text, dest="de")
        await message.answer(tarjima.text, reply_markup=menu)
    elif lang == "de German - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=menu)
    await Translate.lang.set()
    # await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)