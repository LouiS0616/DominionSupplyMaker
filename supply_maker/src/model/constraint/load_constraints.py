from os import PathLike
from typing import Dict, List
import yaml

from supply_maker.src.model.constraint import comply_with_constraint, parse_constraint
from supply_maker.src.model.constraint import SupplyConstraint
from supply_maker.src.model.card.attr.extension_name import ExtensionName


#
def _load_constraint(fp):
    data = yaml.load(fp, yaml.SafeLoader)
    constraint = SupplyConstraint(lambda _: True)

    #
    ex: Dict['ExtensionName', List[int]] = {
        ExtensionName(ex_name): parse_constraint(v) for ex_name, v in data['expansion'].items()
    }
    for e_name, acceptable_count in ex.items():
        constraint &= comply_with_constraint(acceptable_count, ex=e_name)

    return constraint


def load_constraint(p: PathLike):
    with open(p, encoding='utf-8') as fin:
        return _load_constraint(fin)


#
def _load_extensions_never_used(fp) -> List['ExtensionName']:
    data = yaml.load(fp, yaml.SafeLoader)

    return [
        ExtensionName(ex_name)
        for ex_name, v in data['expansion'].items()
        if parse_constraint(v) == [0]
    ]


def load_extensions_never_used(p: PathLike) -> List['ExtensionName']:
    with open(p, encoding='utf-8') as fin:
        return _load_extensions_never_used(fin)
