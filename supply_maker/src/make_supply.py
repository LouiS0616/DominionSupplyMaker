from os import PathLike

from supply_maker.src.model.card_set import Supply
from supply_maker.src.model.constraint.load_constraints import load_constraint, load_extensions_never_used
from supply_maker.src.model.load_cards import load_cards
from supply_maker import _where


def make_supply(constraint_p: PathLike, *, logger=None) -> 'Supply':
    card_set = load_cards(
        _where / 'res/kingdom_cards',
        extensions_never_used=load_extensions_never_used(constraint_p)
    )

    constraint = load_constraint(constraint_p)

    i = 0
    while i < 10_000:
        supply = Supply.frm(card_set, logger=logger)
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