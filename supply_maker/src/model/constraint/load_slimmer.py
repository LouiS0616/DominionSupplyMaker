from os import PathLike
from typing import List, TextIO, TYPE_CHECKING

import yaml

from supply_maker.src.model.card.attr import ExpansionName
from supply_maker.src.model.card.evaluate import CardEvaluator, has_attr
from .candidate_slimmer import CandidateSlimmer
from .parse import parse_constraint
if TYPE_CHECKING:
    from supply_maker.src.model.card_set import CardSet


#
def _load_slimmer(fp: TextIO) -> CandidateSlimmer:
    data = yaml.load(fp, Loader=yaml.SafeLoader)
    assert data.keys() <= {'expansion', }

    # return True if the card will never be used
    predicate_false = CardEvaluator(lambda _: False)

    #
    unused_exs: List['ExpansionName'] = [
        ExpansionName(ex_name) for ex_name, v in data['expansion'].items()
        if parse_constraint(v) == [0]
    ]
    for ex in unused_exs:
        predicate_false |= has_attr(ex=ex)

    #
    class _CandidateSlimmer(CandidateSlimmer):
        def slim(self, candidate: 'CardSet') -> 'CardSet':
            return candidate.filter(
                lambda card: not predicate_false(card)
            )

    return _CandidateSlimmer()


def load_slimmer(p: PathLike) -> CandidateSlimmer:
    with open(p, encoding='utf-8') as fin:
        return _load_slimmer(fin)
