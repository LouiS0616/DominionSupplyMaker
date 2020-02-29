from typing import Dict

from ..attr.card_name import CardName as EffectName
from ..attr.cost import Costless
from ..attr.edition import Edition
from ..attr.effect_type import EffectType
from ..attr.expansion import Expansion
from ._effect_meta import _EffectImpl, _EffectMeta


class Landmark(metaclass=_EffectMeta):
    _cache: Dict[str, 'Landmark'] = {}

    def __init__(self, _impl):
        self._impl = _impl

    @classmethod
    def create(cls,
               ex: str, edition: str, name: str):

        if name in cls._cache:
            return cls._cache[name]

        impl = _EffectImpl(
            Expansion(ex), Edition(edition), EffectType('Landmark'),
            EffectName(name), cost=Costless()
        )
        return Landmark(impl)

    def __getattr__(self, item):
        cls = type(self)
        if item in cls.attrs:
            return getattr(self._impl, item)

        raise AttributeError(f"'Landmark' object has no attribute '{item}'.")

    def __str__(self):
        return '{ex}{edition}: ({typ}) {name}'.format(
            ex=self.ex.t(),
            edition='' if self.edition.is_newest() else f'({self.edition})',
            typ=self.typ.t(),
            name=self.name.t()
        )
