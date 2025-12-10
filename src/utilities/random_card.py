from random import choice, random

from src.common.dto.card import Card
from src.common.enum.tarocard import TarotCard


def weighted_bool(true_chance: float) -> bool:
    return random() < true_chance

def get_random_cards(count : int, inverted_chance : bool) -> list[Card]:
    cards = set()
    data = list(TarotCard)
    if len(data) < count:
        raise Exception("There are not enough cards in the set to choose from")
    while len(cards) != count:
        card = Card(photo_id=choice(data).jpg, inverted=weighted_bool(inverted_chance))
        cards.add(card)
    return list(cards)