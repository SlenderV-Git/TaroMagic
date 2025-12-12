from aiogram import Router
from .echo import rt as echo_router


def get_root_router():
    rt = Router()
    rt.include_router(echo_router)
    return rt