from abc import ABC, abstractmethod


#
class _ImplAsSet(ABC):
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

    #
    @property
    @abstractmethod
    def data(self): ...

    # noinspection PyPep8Naming
    @property
    @abstractmethod
    def _Seq_builder(self): ...
