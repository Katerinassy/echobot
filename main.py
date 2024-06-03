from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет,я твой первый эхо бот')


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer('Привет,я твой первый эхо бот')

@dp.message_handler()
async def echo(message: types.Message):
    await  message.answer(message.text)