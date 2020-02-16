from typing import TextIO

from supply_maker.src.model.card_set import Supply
from supply_maker.src.model.constraint.load_constraints import load_constraint, load_extensions_never_used
from supply_maker.src.model.load_cards import load_cards
from . import _where, get_file_logger


# noinspection SpellCheckingInspection
_supply_logger = get_file_logger(
    'supply', form='%(levelname)s | %(message)s'
)


def make_supply(constraint_fp: TextIO) -> 'Supply':
    card_set = load_cards(
        _where / 'res/kingdom_cards',
        extensions_never_used=load_extensions_never_used(constraint_fp)
    )
    constraint_fp.seek(0)

    #
    constraint = load_constraint(constraint_fp)

    i = 0
    while i < 10_000:
        supply = Supply.frm(card_set, logger=_supply_logger)
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
