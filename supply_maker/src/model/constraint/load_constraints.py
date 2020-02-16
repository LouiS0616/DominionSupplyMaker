from typing import Dict, List, TextIO
import yaml

from supply_maker.src.model.constraint import comply_with_constraint, parse_constraint
from supply_maker.src.model.constraint import SupplyConstraint
from supply_maker.src.model.card.attr.extension_name import ExtensionName


def load_constraint(fp: TextIO):
    data = yaml.load(fp, yaml.SafeLoader)
    constraint = SupplyConstraint(lambda _: True)

    #
    ex: Dict[ExtensionName, List[int]] = {
        ExtensionName(ex_name): parse_constraint(v) for ex_name, v in data['expansion'].items()
    }
    for e_name, acceptable_count in ex.items():
        constraint &= comply_with_constraint(acceptable_count, ex=e_name)

    return constraint

