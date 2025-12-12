import logging
from typing import Annotated
from fastapi import APIRouter, Depends, Request
from aiogram.types import Update
from aiogram import Bot, Dispatcher

from src.api.common.providers.stub import Stub


update_router = APIRouter(tags=["webhook"])
logger = logging.getLogger(__name__)

@update_router.post("/webhook/")
async def handle_update(
    request : Request,
    bot : Annotated[Bot, Depends(Stub(Bot))],
    dp : Annotated[Dispatcher, Depends(Stub(Dispatcher))]
    ):
    logger.critical(str(request))
    update = Update.model_validate(
        await request.json(),
        context={"bot":bot}
    )
    await dp.feed_update(bot, update)
    return {"ok": True}