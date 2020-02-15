from typing import TYPE_CHECKING
from typing import Callable, Dict, List

from ..card import Card, Cost
from ..card.attr.card_name import CardName
from ..card.evaluate import has_attr
from ..card_set import CardSet
from .role import Role

SupplySetUpper = Callable[
    [Callable[[Card], None], CardSet, Dict[Card, Role], List[str]],
    None
]

if TYPE_CHECKING:
    from ..card_set import Supply


#
def setup_by_young_witch(
        card_adder, candidates: CardSet,
        card_to_role: Dict[Card, Role], _: List[str]) -> None:

    """!BANG FUNCTION!"""
    #assert supply.contains(CardName('Young Witch'))
    #assert (supply & candidates).empty()

    bane = candidates.filter(
        has_attr(cost=Cost(2)) | has_attr(cost=Cost(3))
    ).any()

    card_adder(bane)
    card_to_role[bane] = Role('Bane')


_set_upper = {
    CardName('Young Witch'): setup_by_young_witch,
}


#
def load(cards: CardSet) -> List[SupplySetUpper]:
    return [
        func
        for name, func in _set_upper.items()
        if cards.contains(name)
    ]
