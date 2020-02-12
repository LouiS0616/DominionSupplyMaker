import operator
import random
from typing import List, TYPE_CHECKING

from sortedcontainers import SortedSet
from supply_maker.src.model.card.evaluate import CardEvaluator, has_attr
if TYPE_CHECKING:
    from supply_maker.src.model.card import Card


class CardSet:
    def __init__(self, *, elms=None):
        self._data = SortedSet(elms, key=operator.attrgetter('cost'))

    def add(self, *elms: 'Card'):
        self._data |= set(elms)

    def any(self) -> 'Card':
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
        return [card.name.t() for card in self._data]

    #
    def contains(self, name) -> bool:
        ev = has_attr(name=name)
        return any(ev(card) for card in self._data)

    def filter(self, evaluator: CardEvaluator) -> 'CardSet':
        return CardSet(
            elms=filter(evaluator, self._data)
        )

    def __len__(self) -> int:
        return len(self._data)

    def empty(self) -> bool:
        return len(self) == 0

    #
    def __and__(self, other: 'CardSet') -> 'CardSet':
        return CardSet(
            elms=self._data & other._data
        )

    def __sub__(self, other: 'CardSet') -> 'CardSet':
        return CardSet(
            elms=self._data - other._data
        )
