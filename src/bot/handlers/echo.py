from aiogram import Router
from aiogram.types import Message


rt = Router()

@rt.message()
async def echo(message : Message):
    await message.answer(message.text)