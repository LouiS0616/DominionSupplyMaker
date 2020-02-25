import dataclasses
from dataclasses import dataclass
from typing import Dict

from supply_maker.src.model.card.attr.edition import Edition
from supply_maker.src.model.card.attr.expansion import Expansion
from supply_maker.src.model.card.attr.cost import Cost
from .attr.effect_name import EffectName
from .attr.effect_type import EffectType


@dataclass(frozen=True)
class _EffectImpl:
    ex:      Expansion
    edition: Edition
    typ:     EffectType
    name:    EffectName
    cost:    Cost


#
class _EffectMeta(type):
    _attrs: [str] = [
        f.name for f in dataclasses.fields(_EffectImpl)
    ]

    @property
    def attrs(cls) -> [str]:
        return cls._attrs[:]


class Effect(metaclass=_EffectMeta):
    _cache: Dict[str, _EffectImpl] = {}

    def __init__(self, impl: _EffectImpl):
        """Private-like initialization method"""
        if not isinstance(impl, _EffectImpl):
            raise ValueError('Card instance should be made by create method.')

        self._impl = impl

    @classmethod
    def create(cls,
               ex: str, edition: str, typ: str, name: str, cost: int):

        if name in cls._cache:
            return Effect(cls._cache[name])

        impl = _EffectImpl(
            Expansion(ex), Edition(edition), EffectType(typ),
            EffectName(name), Cost(cost)
        )
        return Effect(impl)

    #
    def __getattr__(self, item):
        cls = type(self)
        if item in cls.attrs:
            return getattr(self._impl, item)

        raise AttributeError(f"'Effect' object has no attribute '{item}'")

    def __str__(self):
        return '{ex}{edition}: ({typ}) {name} - {cost}'.format(
            ex=self.ex.t(),
            edition='' if self.edition.is_newest() else f'({self.edition})',
            typ=self.typ.t(),
            name=self.name.t(),
            cost=self.cost
        )
