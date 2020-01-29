import dataclasses
from dataclasses import dataclass
from typing import Dict

from .cost import Cost


@dataclass(frozen=True)
class _CardImpl:
    ex:   str           # 拡張名
    name: str
    cost: Cost

    is_action:   bool
    is_attack:   bool
    is_reaction: bool
    is_duration: bool   # 持続

    is_treasure: bool   # 財宝
    is_victory:  bool   # 勝利点


#
# Ref. https://stackoverflow.com/questions/128573/using-property-on-classmethods
class _CardMeta(type):
    _attrs: [str] = [
        f.name for f in dataclasses.fields(_CardImpl)
    ]

    @property
    def attrs(cls) -> [str]:
        return cls._attrs[:]


class Card(metaclass=_CardMeta):
    _cache: Dict[str, _CardImpl] = {}

    def __init__(self, impl: _CardImpl):
        self._impl = impl

    @classmethod
    def create(cls,
               ex: str, name: str, cost_coin: int, need_potion: bool,
               is_action: bool, is_attack: bool, is_reaction: bool, is_duration: bool,
               is_treasure: bool, is_victory: bool) -> 'Card':

        if name in cls._cache:
            return Card(cls._cache[name])

        impl = _CardImpl(
            ex, name, Cost(cost_coin, need_potion),
            is_action, is_attack, is_reaction, is_duration,
            is_treasure, is_victory
        )
        return Card(impl)

    #
    def __getattr__(self, item):
        cls = type(self)
        if item in cls.attrs:
            return getattr(self._impl, item)

        raise AttributeError(f"'Card' object has no attribute '{item}'")

    #
    def __str__(self):
        return '{ex}: {name} - {cost} - {card_type}'.format(
            ex=self.ex,
            name=self.name,
            cost=self.cost,
            card_type=' / '.join(filter(None, [
                'action'   if self.is_action   else '',
                'attack'   if self.is_attack   else '',
                'reaction' if self.is_reaction else '',
                'duration' if self.is_duration else '',
                'treasure' if self.is_treasure else '',
                'victory'  if self.is_victory  else '',
            ]))
        )
