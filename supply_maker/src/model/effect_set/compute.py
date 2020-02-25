from typing import List
from typing import TYPE_CHECKING

from supply_maker.src.util.combination import combination
if TYPE_CHECKING:
    from supply_maker.src.model.card_set.candidates import Candidates as SupplyCandidates
    from supply_maker.src.model.effect_set.effect_candidates import EffectCandidates


def _compute_effect_appearance(s, n, m, d) -> float:
    """
    Parameters
    ----------
    d : int

    Returns
    -------
    ret : float
        the rate: JUST d pieces of effects will be chosen.
    """

    # the rate of d effects will be chosen when (s+d)-1 cards are drawn.
    term1 = (combination(n, s-1) * combination(m, d)) / combination(n+m, s+d-1)

    # the rate of the last-chosen card is kingdom.
    term2 = (n - (s-1)) / (n + m - (s-1) - d)

    return term1 * term2


def _compute_effect_balance(s, n, m, max_: int) -> List[float]:
    """
    Parameters
    ----------
    s : int
        size of supply, normally 10.
    n : int
        num of supply-candidates.
    m : int
        num of effect-candidates.
    max_ : int

    Returns
    -------
    probabilities : [float]
        [prob 0 effect is selected, prob 1, ..., prob max_ or more]
    """

    ret = [
        _compute_effect_appearance(s, n, m, d) for d in range(max_)
    ]
    assert sum(ret) <= 1.

    return ret + [1 - sum(ret)]


#
def compute_effect_balance(
        supply_candidates: 'SupplyCandidates',
        effect_candidates: 'EffectCandidates', *, num_of_supply=10, max_) -> List[float]:

    """
    Parameters
    ----------
    supply_candidates : Candidates
        it must be the entire candidates, including cards which has already chosen.
    """

    return _compute_effect_balance(
        num_of_supply, len(supply_candidates), len(effect_candidates), max_
    )
