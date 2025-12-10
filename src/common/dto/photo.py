from src.common.dto.base import DTO

class Photo(DTO):
    photo_id : str
    bytes_data : bytes

    def save(self, path : str):
        with open(f"{path}/{self.photo_id}", "wb") as file:
            file.write(self.bytes_data)