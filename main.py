import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InputFile
from aiogram.utils import executor
from resizer import resize_image

API_TOKEN = 'your_token_here'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
   await msg.answer("Assalomu alaykum botimga hush kelibsiz\nBotdan foydalanish uchun shunchaki jpg yoki png formatdagi rasim jo'nating")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def process_image(message: types.Message):
    user_id = message.from_user.id
    photo = message.photo[-1]
    input_photo = f"input.jpg"
    await photo.download(input_photo)

    resized_path = resize_image(input_photo)
    
    recipient_id = message.from_user.id
    
    await bot.send_photo(chat_id=recipient_id, photo=InputFile('output.jpg'))

    os.remove(input_photo)
    os.remove('output.jpg')


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
