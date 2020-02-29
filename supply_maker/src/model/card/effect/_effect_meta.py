import dataclasses
from dataclasses import dataclass
from typing import List

from ..attr.card_name import CardName as EffectName
from ..attr.cost import CostType
from ..attr.edition import Edition
from ..attr.effect_type import EffectType
from ..attr.expansion import Expansion


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
