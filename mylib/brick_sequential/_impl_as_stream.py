from abc import ABC, abstractmethod
import random

from ._impl_base import _ImplBase


#
class _ImplAsStream(_ImplBase, ABC):
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
