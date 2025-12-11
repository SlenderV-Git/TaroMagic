from fastapi import APIRouter

from src.api.v1.endpoints import (
    healthcheck_router,
    auth_router,
    user_router
)


def init_v1_routers() -> APIRouter:
    app = APIRouter(prefix="/v1")

    app.include_router(healthcheck_router, prefix="/healthcheck")
    app.include_router(auth_router, prefix="/auth")
    app.include_router(user_router, prefix="/user")

    return app