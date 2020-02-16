from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supply_maker.src.model.card_set import CardSet


#
class CandidateSlimmer(ABC):
    @abstractmethod
    def slim(self, candidate: 'CardSet') -> 'CardSet':  ...
