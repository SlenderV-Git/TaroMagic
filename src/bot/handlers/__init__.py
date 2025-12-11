from aiogram import Dispatcher
from .echo import rt as echo_router


def get_root_dispather():
    dp = Dispatcher()
    dp.include_router(echo_router)
    return dp