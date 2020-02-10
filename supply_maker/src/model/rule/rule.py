from typing import TYPE_CHECKING
from typing import Callable, Dict, List

from ..card import Card, Cost
from ..card.attr.card_name import CardName
from ..card.evaluate import has_attr
from ..card_set import CardSet

SupplySetUpper = Callable[
    ['Supply', CardSet, Dict[Card, str], List[str]],
    None
]

if TYPE_CHECKING:
    from ..card_set import Supply


# 魔女娘
def setup_by_young_witch(
        supply: 'Supply', candidates: CardSet,
        card_to_role: Dict[Card, str], _: List[str]) -> None:

    """!BANG FUNCTION!"""
    # todo: 英語に差し替える
    assert supply.contains(CardName('Young Witch'))
    assert (supply & candidates).empty()

    bane = candidates.filter(
        has_attr(cost=Cost(2)) | has_attr(cost=Cost(3))
    ).any()

    supply.add(bane)
    card_to_role[bane] = '災い'


_set_upper = {
    CardName('Young Witch'): setup_by_young_witch,
}


def load(cards: CardSet) -> List[SupplySetUpper]:
    return [
        func
        for name, func in _set_upper.items()
        if cards.contains(name)
    ]
