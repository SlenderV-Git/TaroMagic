from typing import Annotated
from fastapi import APIRouter, Depends
from aiogram.types import Update
from aiogram import Bot, Dispatcher

from src.bot.handlers import get_root_dispather


update_router = APIRouter(tags=["webhook"])


@update_router.post("/webhook")
async def handle_update(
    update : Update, 
    bot : Annotated[Bot, Depends()],
    dp : Annotated[Dispatcher, Depends(get_root_dispather)]
    ):
    await dp.feed_update(bot, update)