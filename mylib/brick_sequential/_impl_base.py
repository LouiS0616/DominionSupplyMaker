from abc import ABC, abstractmethod


#
class _ImplBase(ABC):
    @property
    @abstractmethod
    def data(self): ...

    # noinspection PyPep8Naming
    @property
    @abstractmethod
    def _Seq_builder(self): ...
