from os import PathLike
from typing import Tuple

from supply_maker.src.model.card_set import Supply
from supply_maker.src.model.constraint.load import load_constraint_and_slimmer
from supply_maker.src.model.load_cards import load_cards


def make_supply(constraint_p: PathLike, *, logger=None) -> Tuple['Supply', int]:
    """
    Returns
    ---
    supply : Supply
        chosen supply complying the constraint

    trial_count : int
        num of trial to make supply
    """
    candidates = load_cards()

    constraint, slimmer = load_constraint_and_slimmer(constraint_p)
    candidates.slim(slimmer)

    trial_count = 0
    while trial_count < 10_000:
        supply = Supply.frm(candidates, logger=logger)
        supply.setup()

        if supply.is_valid(constraint):
            break

        trial_count += 1
    else:
        raise ValueError('\n'.join([
            'Though system has tried to make supply 10,000 times, cannot complete that.',
            'Check constraint, that should be too tight.'
        ]))

    return supply, trial_count
