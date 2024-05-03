from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart
import asyncio
from aiogram import F
import os
from rembg import remove
from PIL import Image
import requests
import time

folder_name = "in_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

token = "6871114067:AAHrDHSIkgPSXBi8vlfPoRLx_MBpUBDPrXQ"
bot = Bot(token=token)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello, I am a bot!')

@dp.message(F.photo)
async def photo(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    width = photo.width
    height = photo.height
    size = photo.file_size
    file = await bot.get_file(file_id=file_id)
    file_path = file.file_path
    url = f"https://api.telegram.org/file/bot{token}/{file_path}"
    print(url)

    folder = "out_image"
    if not os.path.exists(folder):
        os.makedirs(folder)
    vaqt = time.time()
    name = f"{folder}/{message.from_user.id}_{vaqt}.png"

    input_path = requests.get(url,stream=True).raw
    output_path = name
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    rasm = types.input_file.FSInputFile(name)
    await message.answer_photo(photo=rasm)

    await bot.download(file=file, destination=f"{folder_name}/{file_id}.jpg")
    await message.answer("Dabdubayo")

    #await message.answer(f'{file_id}\n{width}\n{he ight}\n{size}\n')
    #await message.answer_photo(photo=file_id)
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())







