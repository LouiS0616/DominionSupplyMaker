from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supply_maker.src.model.card_set import Candidates


#
class CandidateSlimmer(ABC):
    @abstractmethod
    def slim(self, candidate: 'Candidates') -> 'Candidates':  ...
