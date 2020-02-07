import operator
import random
from typing import List

from sortedcontainers import SortedSet
from ..card import Card
from ..card.evaluate import CardEvaluator, has_attr


class CardSet:
    def __init__(self, *, _frm: 'CardSet' = None, elms=None):
        if _frm is None:
            self._data = SortedSet(elms, key=operator.attrgetter('cost'))
        else:
            assert elms is None
            self._data = _frm._data.copy()

    def add(self, *elms: Card):
        self._data |= set(elms)

    def any(self) -> Card:
        return self.choose(1)._data[0]

    def choose(self, k) -> 'CardSet':
        return CardSet(
            elms=random.sample(self._data, k)
        )

    #
    def __str__(self):
        return '\n'.join(self.names)

    @property
    def names(self) -> List[str]:
        return [str(card.name) for card in self._data]

    #
    def contains(self, name: str) -> bool:
        ev = has_attr(name=name)
        return any(ev(card) for card in self._data)

    def filter(self, evaluator: CardEvaluator) -> 'CardSet':
        return CardSet(
            elms=filter(evaluator, self._data)
        )

    def empty(self) -> bool:
        return not self

    def __and__(self, other: 'CardSet') -> 'CardSet':
        return CardSet(
            elms=self._data & other._data
        )

    def __sub__(self, other: 'CardSet') -> 'CardSet':
        return CardSet(
            elms=self._data - other._data
        )

    #
    def __len__(self):
        return len(self._data)
