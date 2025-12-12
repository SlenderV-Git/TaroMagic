from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from bot.handlers import get_root_router
from src.api.setup import init_app, start_app
from src.core.settings import (
    get_bot_settings,
    get_db_settings,
    get_documentation_settings,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    bot : Bot = app.dependency_overrides[Bot]()
    await bot.set_webhook(url=get_bot_settings().WEBHOOK, drop_pending_updates=True)
    yield
    await bot.delete_webhook()

def main() -> None:
    db_settings = get_db_settings()
    doc_settings = get_documentation_settings()
    
    app = init_app(db_settings, doc_settings, lifespan=lifespan)
    dp : Dispatcher = app.dependency_overrides[Dispatcher]()
    dp.include_router(get_root_router())
    
    start_app(app)


if __name__ == "__main__":
    main()