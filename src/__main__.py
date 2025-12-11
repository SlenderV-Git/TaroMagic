import asyncio

from aiogram import Bot
from src.api.setup import init_app, start_app
from src.core.settings import (
    get_bot_settings,
    get_db_settings,
    get_documentation_settings,
)


def main() -> None:
    db_settings = get_db_settings()
    doc_settings = get_documentation_settings()
    
    
    app = init_app(db_settings, doc_settings)
    
    start_app(app)
    bot : Bot = app.dependency_overrides[Bot]
    asyncio.run(bot.set_webhook(get_bot_settings().WEBHOOK))


if __name__ == "__main__":
    main()