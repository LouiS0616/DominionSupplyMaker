from typing import Dict, List, TYPE_CHECKING

from supply_maker.src.model.card import Card, Cost
from supply_maker.src.model.constraint.constraint import has_attr
from .role import Role
from ._set_upper import register_set_upper

if TYPE_CHECKING:
    from supply_maker.src.model.card_set import Candidates
    from ._set_upper import SupplySetUpper


#
@register_set_upper('Young Witch')
def _setup_by_young_witch(
        add_cards, candidates: 'Candidates',
        card_to_role: Dict['Card', 'Role'], _: List[str]) -> None:

    bane = candidates.filter(
        has_attr(cost=Cost(2)) | has_attr(cost=Cost(3))
    ).any()

    add_cards(bane)
    card_to_role[bane] = Role('Bane')


#
def load_set_uppers() -> Dict['Card', 'SupplySetUpper']:
    from ._set_upper import _set_uppers
    return _set_uppers.copy()
