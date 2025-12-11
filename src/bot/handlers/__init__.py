from aiogram import Dispatcher
from .echo import rt as echo_router


def get_root_dispather():
    dp = Dispatcher()
    try:
        dp.include_router(echo_router)
    except:
        pass
    return dp