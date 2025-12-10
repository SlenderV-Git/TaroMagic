from src.common.dto.base import DTO


class Card(DTO):
    photo_id : str
    inverted : bool

    def __eq__(self, other):
        return isinstance(other, Card) and self.photo_id == other.photo_id and self.inverted == other.inverted

    def __hash__(self):
        return hash((self.photo_id, self.inverted))