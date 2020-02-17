from abc import ABC, abstractmethod
from typing import Dict, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supply_maker.src.model.card.card import Card
    from supply_maker.src.model.preparation.role import Role


class SupplyPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print_supply(
            *,
            cards: List['Card'],
            card_to_role: Dict['Card', 'Role'],
            notes: List[str]):

        ...


class DefaultSupplyPrinter(SupplyPrinter):
    @staticmethod
    def print_supply(
            *,
            cards: List['Card'],
            card_to_role: Dict['Card', 'Role'],
            notes: List[str]):

        s = '\n'.join(
            '{} {} {}'.format(
                card.cost, card.name.t(),
                '({})'.format(card_to_role[card].t()) if card in card_to_role else ''
            )
            for card in cards
        )
        print(s)
