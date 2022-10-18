from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Uzb - 🇬🇧 Eng"), KeyboardButton(text="🇬🇧 Eng - 🇺🇿 Uzb")],
        #[KeyboardButton(text="🇺🇿 Uzb - 🇷🇺 Rus"), KeyboardButton(text="🇷🇺 Rus - 🇺🇿 Uzb")],
        #[KeyboardButton(text="🇺🇿 Uzb - fr French "), KeyboardButton(text="fr French - 🇺🇿 Uzb")],
        [KeyboardButton(text="🇺🇿 Uzb - de German "), KeyboardButton(text="de German - 🇺🇿 Uzb")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)