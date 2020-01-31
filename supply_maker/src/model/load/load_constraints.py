from typing import Dict, List
import yaml

from .... import _where
from ..constraint import comply_with_constraint, parse_constraint
from ..constraint import SupplyConstraint


def load_constraint() -> SupplyConstraint:
    return _constraint


def _init():
    path = _where / 'res/constraints.yml'
    with open(path, encoding='utf-8') as fin:
        data = yaml.load(fin, yaml.SafeLoader)

    constraint = SupplyConstraint(lambda _: True)

    #
    ex: Dict[str, List[int]] = {
        ex_name: parse_constraint(v) for ex_name, v in data['expansion'].items()
    }
    for e_name, acceptable_count in ex.items():
        constraint &= comply_with_constraint(acceptable_count, ex=e_name)

    return constraint


_constraint = _init()
