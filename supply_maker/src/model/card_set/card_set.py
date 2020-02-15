import operator

from sortedcontainers import SortedSet

from . import _card_set_impl
from ._card_set_impl import _ImplAsCollection, _ImplAsSet, _ImplAsStream


#
class CardSet(_ImplAsSet, _ImplAsStream, _ImplAsCollection):
    def __init__(self, *, elms=None):
        self._data = SortedSet(elms, key=operator.attrgetter('cost'))

    @property
    def data(self) -> SortedSet:
        return self._data.copy()


_card_set_impl.CardSet = CardSet
