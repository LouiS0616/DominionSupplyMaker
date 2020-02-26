from supply_maker.src.model.card.attr.edition import Edition
from supply_maker.src.model.card.attr.expansion import Expansion
from .effect import _EffectImpl
from .effect import Effect
from .attr.effect_name import EffectName
from .attr.effect_type import EffectType


class Landmark(Effect):
    def __init__(self, _impl):
        super().__init__(_impl)

    @classmethod
    def create(cls,
               ex: str, edition: str, name: str, *, cost):

        impl = _EffectImpl(
            Expansion(ex), Edition(edition), EffectType('Landmark'),
            EffectName(name), cost=None
        )
