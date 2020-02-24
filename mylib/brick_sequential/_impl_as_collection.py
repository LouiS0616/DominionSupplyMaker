from abc import ABC, abstractmethod


#
class _ImplAsCollection(ABC):
    def __len__(self) -> int:
        return len(self.data)

    def empty(self) -> bool:
        return len(self) == 0

    #
    @property
    @abstractmethod
    def data(self): ...
