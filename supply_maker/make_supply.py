from typing import TYPE_CHECKING

from . import _where, get_file_logger
from supply_maker.src.model.load_cards import load_cards
from .src.model.card_set import Supply

if TYPE_CHECKING:
    from .src.model.constraint import SupplyConstraint


_card_set = load_cards(_where / 'res/kingdom_cards')
# noinspection SpellCheckingInspection
_supply_logger = get_file_logger(
    'supply', form='%(levelname)s | %(message)s'
)


def make_supply(constraint: 'SupplyConstraint') -> 'Supply':
    i = 0
    while i < 10_000:
        supply = Supply.frm(_card_set, logger=_supply_logger)
        supply.setup()

        if supply.is_valid(constraint):
            break

        i += 1
    else:
        raise ValueError('\n'.join([
            'Though system has tried to make supply 10,000 times, cannot complete that.',
            'Check constraint, that should be too tight.'
        ]))

    return supply
