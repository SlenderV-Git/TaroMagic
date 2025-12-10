from contextlib import AsyncExitStack
from aiobotocore.session import AioSession
from src.core.settings import get_s3_settings

class MinioManager:
    def __init__(self):
        self._exit_stack = AsyncExitStack()
        self._s3_client = None

    async def __aenter__(self):
        session = AioSession()
        settings = get_s3_settings()
        self._s3_client = await self._exit_stack.enter_async_context(
            session.create_client(
                's3',
                endpoint_url=settings.URL,
                aws_access_key_id=settings.ROOT_USER,
                aws_secret_access_key=settings.ROOT_PASSWORD
            )
        )
        return self._s3_client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._exit_stack.__aexit__(exc_type, exc_val, exc_tb)
        
async def get_minio_client():
    async with MinioManager() as client:
        return client