from abc import ABC, abstractmethod
import random
from typing import Callable, TYPE_CHECKING

from sortedcontainers import SortedSet
from supply_maker.src.model.card.evaluate.card_evaluater import has_attr
if TYPE_CHECKING:
    from supply_maker.src.model.card.attr.card_name import CardName
    from supply_maker.src.model.card.card import Card
    from supply_maker.src.model.card.evaluate.card_evaluater import CardEvaluator

CardSet: Callable[[set], 'CardSet']


#
class _ImplAsSet(ABC):
    def __and__(self, other: '_ImplAsSet') -> 'CardSet':
        return CardSet(
            elms=self.data & other.data
        )

    def __sub__(self, other: '_ImplAsSet') -> 'CardSet':
        return CardSet(
            elms=self.data - other.data
        )

    @property
    @abstractmethod
    def data(self) -> SortedSet:   ...


class _ImplAsStream(ABC):
    def filter(self, evaluator: 'CardEvaluator') -> 'CardSet':
        return CardSet(
            elms=filter(evaluator, self.data)
        )

    def choose(self, k) -> 'CardSet':
        return CardSet(
            elms=random.sample(self.data, k)
        )

    def any(self) -> 'Card':
        return self.choose(1).data[0]

    @property
    @abstractmethod
    def data(self) -> SortedSet:   ...


class _ImplAsCollection(ABC):
    def contains(self, name: 'CardName') -> bool:
        ev = has_attr(name=name)
        return any(
            ev(card) for card in self.data
        )

    def __len__(self) -> int:
        return len(self.data)

    def empty(self) -> bool:
        return len(self) == 0

    @property
    @abstractmethod
    def data(self) -> SortedSet:    ...
