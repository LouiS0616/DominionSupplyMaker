from typing import Callable
from ..card import Card

_CardEvaluator = Callable[['Card'], bool]


class CardEvaluator(_CardEvaluator):
    def __init__(self, pred):
        self._pred = pred

    def __or__(self, other: 'CardEvaluator'):
        def _inner(card: Card) -> bool:
            return self(card) or other(card)

        return CardEvaluator(_inner)

    def __and__(self, other: 'CardEvaluator') -> 'CardEvaluator':
        def _inner(card: Card) -> bool:
            return self(card) and other(card)

        return CardEvaluator(_inner)

    def __call__(self, card: Card) -> bool:
        return self._pred(card)


def has_attr(**kwargs) -> CardEvaluator:
    if not kwargs:
        return CardEvaluator(lambda _: True)

    (attr, value), *kvs = kwargs.items()
    if attr not in Card.attrs:
        raise AttributeError(f"'Card' object has no attribute '{attr}'")

    #
    def _inner(card: 'Card') -> bool:
        return getattr(card, attr) == value

    return CardEvaluator(_inner) & has_attr(**dict(kvs))
