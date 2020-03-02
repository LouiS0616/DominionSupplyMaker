from typing import Dict, TYPE_CHECKING

from ..attr.card_name import CardName as EffectName
from ..attr.cost import Cost, Costless, CostType
from ..attr.edition import Edition
from ..attr.effect_type import EffectType
from ..attr.expansion import Expansion
from ._effect_meta import _EffectImpl, _EffectMeta


class Effect(metaclass=_EffectMeta):
    _cache: Dict[str, 'Effect'] = {}

    def __init__(self, _impl):
        self._impl = _impl

    @classmethod
    def _create(cls,
                ex: str, edition: str, typ: str, name: str, cost: 'CostType'):

        if name in cls._cache:
            return cls._cache[name]

        impl = _EffectImpl(
            Expansion(ex), Edition(edition), EffectType(typ.capitalize()),
            EffectName(name), cost
        )

        cls._cache[name] = Effect(impl)
        return cls._cache[name]

    @classmethod
    def create(cls,
               ex: str, edition: str, typ: str, name: str, cost: int, debt: int):

        return cls._create(
            ex, edition, typ, name, Cost(cost, debt=debt)
        )

    @classmethod
    def create_costless(cls,
                        ex: str, edition: str, typ: str, name: str):

        return cls._create(
            ex, edition, typ, name, Costless()
        )

    # noinspection PyProtectedMember
    @classmethod
    def load(cls, name: 'EffectName'):
        if name._raw_name not in cls._cache:
            raise ValueError(f"cannot load card; {name._raw_name}")

        return cls._cache[name._raw_name]

    #
    def __getattr__(self, item):
        cls = type(self)
        if item in cls.attrs:
            return getattr(self._impl, item)

        raise AttributeError(f"'Effect' object has no attribute '{item}'.")

    #
    def __str__(self):
        return '{ex}{edition}: ({typ}) {name}{cost}'.format(
            ex=self.ex.t(),
            edition='' if self.edition.is_newest() else f'({self.edition})',
            typ=self.typ.t(),
            name=self.name.t(),
            cost='' if isinstance(self.cost, Costless) else f' - {self.cost}'
        )
