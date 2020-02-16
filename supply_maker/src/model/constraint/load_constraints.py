from os import PathLike
from typing import Dict, List
import yaml

from supply_maker.src.model.constraint import comply_with_constraint, parse_constraint
from supply_maker.src.model.constraint import SupplyConstraint
from supply_maker.src.model.card.attr.expansion_name import ExpansionName


#
def _load_constraint(fp):
    data = yaml.load(fp, yaml.SafeLoader)
    assert data.keys() <= {'expansion', }

    constraint = SupplyConstraint(lambda _: True)

    #
    ex: Dict['ExpansionName', List[int]] = {
        ExpansionName(ex_name): parse_constraint(v) for ex_name, v in data['expansion'].items()
    }
    for e_name, acceptable_count in ex.items():
        constraint &= comply_with_constraint(acceptable_count, ex=e_name)

    return constraint


def load_constraint(p: PathLike):
    with open(p, encoding='utf-8') as fin:
        return _load_constraint(fin)


#
def _load_expansions_never_used(fp) -> List['ExpansionName']:
    data = yaml.load(fp, yaml.SafeLoader)

    return [
        ExpansionName(ex_name)
        for ex_name, v in data['expansion'].items()
        if parse_constraint(v) == [0]
    ]


def load_expansions_never_used(p: PathLike) -> List['ExpansionName']:
    with open(p, encoding='utf-8') as fin:
        return _load_expansions_never_used(fin)
