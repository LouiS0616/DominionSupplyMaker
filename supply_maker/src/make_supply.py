from os import PathLike
import random
from typing import Tuple, TYPE_CHECKING

from supply_maker.src.model.card.evaluate.functions import belongs_to_newest_edition
from supply_maker.src.model.card_set.supply import Supply
from supply_maker.src.model.constraint.load import load_constraint_and_slimmer
from supply_maker.src.model.effect_set.compute import compute_effect_balance
from supply_maker.src.model.load_cards import load_cards
from supply_maker.src.model.load_effects import load_effects
if TYPE_CHECKING:
    from supply_maker.src.model.card_set.candidates import Candidates
    from supply_maker.src.model.effect_set.effect_set import EffectSet


def choose_effects(
        supply_candidates: 'Candidates', effect_candidates: 'EffectSet', max_):

    effect_balance = compute_effect_balance(
        supply_candidates, effect_candidates, max_=max_
    )
    num_of_effect, = random.choices(
        [*range(0, max_+1)], effect_balance, k=1
    )

    return effect_candidates.choose(num_of_effect)


def make_supply(constraint_p: PathLike, *, logger=None) -> Tuple['Supply', 'EffectSet', int]:
    """
    Returns
    ---
    supply : Supply
        chosen supply complying the constraint

    trial_count : int
        num of trial to make supply
    """
    # todo: prepare Option to either use 1st edition cards or not.
    candidates = load_cards()       # .filter(belongs_to_newest_edition())
    effects_candidates = load_effects()

    constraint, slimmer = load_constraint_and_slimmer(constraint_p)
    candidates.slim(slimmer)

    # todo: enable to choose effect items; events, landmarks and projects.
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

    #
    effects = choose_effects(
        candidates, effects_candidates, max_=2
    )

    return supply, effects, trial_count
