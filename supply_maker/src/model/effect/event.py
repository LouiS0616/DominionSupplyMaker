from typing import Dict

from supply_maker.src.model.card.attr.cost import Cost
from supply_maker.src.model.card.attr.edition import Edition
from supply_maker.src.model.card.attr.expansion import Expansion
from supply_maker.src.model.effect.attr.effect_name import EffectName
from supply_maker.src.model.effect.attr.effect_type import EffectType
from ._effect_meta import _EffectImpl, _EffectMeta


class Event(metaclass=_EffectMeta):
    _cache: Dict[str, 'Event'] = {}

    def __init__(self, _impl):
        self._impl = _impl

    @classmethod
    def create(cls,
               ex: str, edition: str, name: str, cost: int, debt: int):

        if name in cls._cache:
            return cls._cache[name]

        impl = _EffectImpl(
            Expansion(ex), Edition(edition), EffectType('Event'),
            EffectName(name), Cost(cost, debt=debt)
        )
        return Event(impl)

    def __getattr__(self, item):
        cls = type(self)
        if item in cls.attrs:
            return getattr(self._impl, item)

        raise AttributeError(f"'Event' object has no attribute '{item}'.")

    def __str__(self):
        return '{ex}{edition}: ({typ}) {name} - {cost}'.format(
            ex=self.ex.t(),
            edition='' if self.edition.is_newest() else f'({self.edition})',
            typ=self.typ.t(),
            name=self.name.t(),
            cost=self.cost
        )
