from abc import ABC
from ._impl_base import _ImplBase


#
class _ImplAsCollection(_ImplBase, ABC):
    def __len__(self) -> int:
        return len(self.data)

    def empty(self) -> bool:
        return len(self) == 0
