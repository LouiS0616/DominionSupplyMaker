from typing import Dict, List, TextIO
import yaml

from ..constraint import comply_with_constraint, parse_constraint
from ..constraint import SupplyConstraint


def load_constraint(fp: TextIO):
    data = yaml.load(fp, yaml.SafeLoader)
    constraint = SupplyConstraint(lambda _: True)

    #
    ex: Dict[str, List[int]] = {
        ex_name: parse_constraint(v) for ex_name, v in data['expansion'].items()
    }
    for e_name, acceptable_count in ex.items():
        constraint &= comply_with_constraint(acceptable_count, ex=e_name)

    return constraint

