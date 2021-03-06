from os import PathLike
from typing import Dict, List, Tuple
import yaml

from supply_maker.src.model.card.attr.expansion import Expansion
from supply_maker.src.model.card.evaluate.card_evaluater import CardEvaluator
from supply_maker.src.model.card.evaluate.functions import has_attr
from .constraint import comply_with_constraint, SupplyConstraint
from .parse_ac_count import parse_constraint
from .slimmer import CandidateSlimmer


#
def load_constraint_and_slimmer(p: PathLike) -> Tuple['SupplyConstraint', 'CandidateSlimmer']:
    with open(p, encoding='utf-8') as fin:
        data = yaml.load(fin, Loader=yaml.SafeLoader)

    assert data.keys() <= {'expansion', }

    #
    constraint = SupplyConstraint(lambda _: True)
    card_unnecessary = CardEvaluator(lambda _: False)   # return True if the card is unnecessary

    #
    ex: Dict['Expansion', List[int]] = {
        Expansion(ex_name): parse_constraint(v) for ex_name, v in data['expansion'].items()
    }
    for ex_name, v in ex.items():
        if v == [0]:
            card_unnecessary |= has_attr(ex=ex_name)

        constraint &= comply_with_constraint(ac_counts=v, ex=ex_name)

    #
    return constraint, CandidateSlimmer(card_unnecessary)
