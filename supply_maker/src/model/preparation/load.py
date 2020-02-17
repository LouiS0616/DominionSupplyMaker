from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from supply_maker.src.model.card import Card
    from ._set_upper import SupplySetUpper


#
def load_set_uppers() -> Dict['Card', 'SupplySetUpper']:
    from ._set_upper_impl import _set_uppers
    return _set_uppers.copy()
