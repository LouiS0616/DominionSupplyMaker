import operator
from typing import TYPE_CHECKING

from sortedcontainers import SortedSet
from mylib.brick_sequential import build_sequential, Impls

from ..card.evaluate.functions import has_attr
if TYPE_CHECKING:
    from ..card.attr.card_name import CardName


#
_CardSetImpl = build_sequential(
    '_CardSetImpl',
    (Impls.AS_COLLECTION, Impls.AS_SET, Impls.AS_STREAM), {},
    builder=lambda x: CardSet(elms=x)
)


class CardSet(_CardSetImpl):
    def __init__(self, *, elms=None):
        self._data = SortedSet(
            elms, key=operator.attrgetter('cost', 'name')
        )

    def contains(self, card_name: 'CardName'):
        ev = has_attr(name=card_name)
        return any(
            ev(card) for card in self.data
        )

    @property
    def data(self) -> SortedSet:
        return self._data.copy()
