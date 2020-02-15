from typing import TYPE_CHECKING
from typing import Callable, Dict, List

from ..card import Card, Cost
from ..card.attr.card_name import CardName
from ..card.evaluate import has_attr
from ..card_set import CardSet
from .role import Role


SupplySetUpper = Callable[
    [
        Callable[[Card], None],     # for adding extra card
        CardSet,                    # candidate
        Dict[Card, Role],           # card to role
        List[str]                   # notes
    ], None
]


def set_upper(func):
    _inner: SupplySetUpper

    def _inner(*, add_card, candidate, card_to_role, notes):
        return func(add_card, candidate, card_to_role, notes)

    return _inner


#
@set_upper
def setup_by_young_witch(
        add_cards, candidates: CardSet,
        card_to_role: Dict[Card, Role], _: List[str]) -> None:

    bane = candidates.filter(
        has_attr(cost=Cost(2)) | has_attr(cost=Cost(3))
    ).any()

    add_cards(bane)
    card_to_role[bane] = Role('Bane')


_set_uppers = {
    CardName('Young Witch'): setup_by_young_witch,
}


#
def load() -> Dict[CardName, SupplySetUpper]:
    return _set_uppers.copy()
