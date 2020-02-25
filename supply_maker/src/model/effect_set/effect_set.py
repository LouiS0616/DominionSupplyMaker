import operator
from sortedcontainers.sortedset import SortedSet

from mylib.brick_sequential import build_sequential, Impls


#
_EffectSetImpl = build_sequential(
    '_EffectSetImpl',
    (Impls.AS_COLLECTION, Impls.AS_SET, Impls.AS_STREAM), {},
    builder=lambda x: EffectSet(elms=x)
)


class EffectSet(_EffectSetImpl):
    def __init__(self, *, elms=None):
        self._data = SortedSet(
            elms, key=operator.attrgetter('typ', 'cost')
        )

    @property
    def data(self):
        return self._data.copy()
