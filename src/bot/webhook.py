import logging
from typing import Annotated, Any
from fastapi import APIRouter, Depends
from aiogram.types import Update
from aiogram import Bot, Dispatcher

from src.api.common.providers.stub import Stub
from src.bot.handlers import get_root_dispather


update_router = APIRouter(tags=["webhook"])
logger = logging.getLogger(__name__)

@update_router.post("/webhook")
async def handle_update(
    request : Any,
    bot : Annotated[Bot, Depends(Stub(Bot))],
    dp : Annotated[Dispatcher, Depends(get_root_dispather)]
    ):
    logger.critical(str(request))
    update = Update.model_validate(
        await request.json(),
        context={"bot":bot}
    )
    await dp.feed_update(bot, update)
    return {"ok": True}