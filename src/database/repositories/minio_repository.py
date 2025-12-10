from typing import Sequence, Awaitable, Type
from types_aiobotocore_s3.client import S3Client
from aiobotocore.response import StreamingBody


from .base.base import BaseRepository
from src.database.models.photo import Photo
from src.database.s3_client import MinioManager


class MinioPhotoRepository(BaseRepository):
    def __init__(self):
        self.manager = MinioManager()
    
    @property
    def model(self) -> Type[Photo]:
        return Photo
    
    async def _init_bucket(self, bucket : str, client : S3Client):
        try:
            await client.head_bucket(Bucket=bucket)
        except Exception as e:
            await client.create_bucket(Bucket=bucket)
            print(e)
            
    async def add(self, bucket : str, photo: Photo) -> Awaitable[None]:
        async with self.manager as client:
            client : S3Client
            await self._init_bucket(bucket, client)
            return await client.put_object(Bucket=bucket,
                              Key=photo.photo_id,
                              Body=photo.bytes_data)
        
    async def __download_photo(self, streaming_body : StreamingBody):
        async with streaming_body as stream:
            data = await stream.read()
        return data
        
    async def get_by_id(self, photo_id: int | str) -> Awaitable[Photo]:
        async with self.manager as client:
            client : S3Client
            resp = await client.get_object(Key=photo_id,
                              Bucket=self.bucket)
            bytes_data = await self.__download_photo(resp.get("Body"))
            return Photo(photo_id=photo_id, bytes_data=bytes_data)
    
    def __is_limit(self, limit : int, index : int):
        if not limit or index < limit:
            return True
        else:
            return False
            
    async def get_all(self, offset : int = 0, limit : int = 0) -> Awaitable[Sequence[Photo]]:
        async with self.manager as client:
            photo_result = []
            client : S3Client
            paginator = client.get_paginator('list_objects')
            index = 0
            async for result in paginator.paginate(Bucket=self.bucket):
                if offset <= index and self.__is_limit(limit, index):
                    content = result.get("Contents")
                    if content:
                        photo_result.extend(content)
            index += 1
            return photo_result
            

    async def delete(self, photo_id: int) -> Awaitable[None]:
        async with self.manager as client:
            client : S3Client
            await client.delete_object(Bucket=self.bucket, Key=photo_id)