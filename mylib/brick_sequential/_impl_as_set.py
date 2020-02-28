from abc import ABC
from ._impl_base import _ImplBase


#
class _ImplAsSet(_ImplBase, ABC):
    def __and__(self, other: '_ImplAsSet') -> '_ImplAsSet':
        return self._Seq_builder(
            self.data & other.data
        )

    def __or__(self, other: '_ImplAsSet') -> '_ImplAsSet':
        return self._Seq_builder(
            self.data | other.data
        )

    def __sub__(self, other: '_ImplAsSet') -> '_ImplAsSet':
        return self._Seq_builder(
            self.data - other.data
        )
