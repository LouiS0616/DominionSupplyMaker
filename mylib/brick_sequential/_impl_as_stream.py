from abc import ABC, abstractmethod
import random


#
class _ImplAsStream(ABC):
    def filter(self, evaluator) -> '_ImplAsStream':
        return self._Seq_builder(
            filter(evaluator, self.data)
        )

    def choose(self, k: int) -> '_ImplAsStream':
        return self._Seq_builder(
            random.sample(self.data, k)
        )

    def any(self):
        ret, = self.choose(1).data
        return ret

    #
    @property
    @abstractmethod
    def data(self): ...

    # noinspection PyPep8Naming
    @property
    @abstractmethod
    def _Seq_builder(self): ...
