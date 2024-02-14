import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    brand_name: str
    card_article: str
    non_existent_article: str


card = Card(
    card_name='Набор ложек чайных Доляна «Симпли», 14,6 см, 6 шт',
    brand_name='Доляна',
    card_article='100056893517',
    non_existent_article='556678341343556'
)


@dataclasses.dataclass
class Texts:
    nothing_found: str = 'Попробуйте поискать по-другому или сократить запрос'
    empty_cart: str = 'В корзине пока пусто'
