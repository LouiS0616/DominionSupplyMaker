from typing import Callable
from supply_maker.src.model.card.gainable.card import Card

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

    @property
    def neg(self) -> 'CardEvaluator':
        return CardEvaluator(lambda card: not self(card))

    def __call__(self, card: Card) -> bool:
        return self._predicate(card)
