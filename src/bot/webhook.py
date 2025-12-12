import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, Request
from aiogram.types import Update
from aiogram import Bot, Dispatcher

from src.core.settings import get_bot_settings
from src.api.common.providers.stub import Stub


update_router = APIRouter(tags=["webhook"])
logger = logging.getLogger(__name__)

@update_router.post("/webhook/")
async def handle_update(
    request : Request,
    bot : Annotated[Bot, Depends(Stub(Bot))],
    dp : Annotated[Dispatcher, Depends(Stub(Dispatcher))],
    x_telegram_bot_api_secret : Annotated[str | None, Header()] = None
    ):
    if get_bot_settings().SECRET == x_telegram_bot_api_secret:
        update = Update.model_validate(
            await request.json(),
            context={"bot":bot}
        )
        await dp.feed_update(bot, update)
        return {"ok": True}
    else:
        raise HTTPException(status_code=403)