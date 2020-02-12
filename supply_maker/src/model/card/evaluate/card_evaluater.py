from typing import Callable
from ..card import Card

_CardEvaluator = Callable[['Card'], bool]


class CardEvaluator(_CardEvaluator):
    def __init__(self, predicate):
        self._predicate = predicate

    def __or__(self, other: 'CardEvaluator'):
        def _inner(card: Card) -> bool:
            return self(card) or other(card)

        return CardEvaluator(_inner)

    def __and__(self, other: 'CardEvaluator') -> 'CardEvaluator':
        def _inner(card: Card) -> bool:
            return self(card) and other(card)

        return CardEvaluator(_inner)

    def __call__(self, card: Card) -> bool:
        return self._predicate(card)


def has_attr(**kwargs) -> CardEvaluator:
    """
    p = has_attr(ex=ExtensionName('Sample'), cost=Cost(3))
    means -> if card c is from ex 'Sample' AND costs just 3, p(c) returns True.

    p = has_attr(cost=Cost(2)) | has_attr(cost=Cost(3))
    means -> if card c costs just 2 OR 3, p(c) returns True.
    """
    if not kwargs:
        return CardEvaluator(lambda _: True)

    (attr, value), *kvs = kwargs.items()
    if attr not in Card.attrs:
        raise AttributeError(f"'Card' object has no attribute '{attr}'")

    #
    def _inner(card: 'Card') -> bool:
        return getattr(card, attr) == value

    return CardEvaluator(_inner) & has_attr(**dict(kvs))
