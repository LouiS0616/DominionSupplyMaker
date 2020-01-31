from typing import TYPE_CHECKING

from .src.model.load import load_cards
from .src.model.card_set import Supply

if TYPE_CHECKING:
    from .src.model.constraint import SupplyConstraint


_card_set = load_cards()


def make_supply(constraint: 'SupplyConstraint') -> 'Supply':
    i = 0
    while i < 10_000:
        supply = Supply.frm(_card_set)
        supply.setup()

        if supply.is_valid(constraint):
            break

        i += 1
    else:
        raise ValueError('\n'.join([
            'Though system has tried to make supply 10000 times, cannot complete.',
            'Check constraint, that should be too tight.'
        ]))

    return supply
