import dataclasses
from dataclasses import dataclass
from typing import List

from supply_maker.src.model.card.attr.edition import Edition
from supply_maker.src.model.card.attr.expansion import Expansion
from supply_maker.src.model.card.attr.cost import CostType
from .attr.effect_name import EffectName
from .attr.effect_type import EffectType


@dataclass(frozen=True)
class _EffectImpl:
    ex:      Expansion
    edition: Edition
    typ:     EffectType
    name:    EffectName
    cost:    CostType


#
class _EffectMeta(type):
    _attrs: List[str] = [
        f.name for f in dataclasses.fields(_EffectImpl)
    ]

    @property
    def attrs(cls) -> List[str]:
        return cls._attrs[:]
