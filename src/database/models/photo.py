from pydantic import BaseModel

class Photo(BaseModel):
    photo_id : str
    bytes_data : bytes