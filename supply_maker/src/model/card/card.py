import dataclasses
from dataclasses import dataclass
from typing import Dict, List

from supply_maker.src.model.card.attr.cost import Cost
from .attr.card_name import CardName
from .attr.card_type import CardType
from .attr.edition import Edition
from .attr.expansion import Expansion


@dataclass(frozen=True)
class _CardImpl:
    ex:      Expansion
    edition: Edition
    name:    CardName
    cost:    Cost

    is_action:   bool
    is_attack:   bool
    is_reaction: bool
    is_duration: bool
    is_command:  bool

    is_treasure: bool
    is_victory:  bool

    additional_types: List[str]


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
        """Private-like initialization method"""
        if not isinstance(impl, _CardImpl):
            raise ValueError('Card instance should be made by create method.')

        self._impl = impl

    @classmethod
    def create(cls,
               ex: str, edition: str, name: str, cost_coin: int, need_potion: bool,
               is_action: bool, is_attack: bool, is_reaction: bool, is_duration: bool, is_command: bool,
               is_treasure: bool, is_victory: bool, additional_types: List[str]) -> 'Card':

        if name in cls._cache:
            return Card(cls._cache[name])

        impl = _CardImpl(
            Expansion(ex), Edition(edition), CardName(name), Cost(cost_coin, need_potion),
            is_action, is_attack, is_reaction, is_duration, is_command,
            is_treasure, is_victory,
            additional_types
        )
        return Card(impl)

    #
    def __getattr__(self, item):
        cls = type(self)
        if item in cls.attrs:
            return getattr(self._impl, item)

        if item.startswith('is_'):
            item = item[3:].lower()
            return item in map(str.lower, self._impl.additional_types)

        raise AttributeError(f"'Card' object has no attribute '{item}'")

    #
    def __str__(self):
        return '{ex}{edition}: {name} - {cost} - {card_types}'.format(
            ex=self.ex.t(),
            edition='' if self.edition.is_newest() else f'({self.edition})',
            name=self.name.t(),
            cost=self.cost,
            card_types=' / '.join(
                CardType(typ).t() for typ in [
                    'action'   if self.is_action   else '',
                    'attack'   if self.is_attack   else '',
                    'reaction' if self.is_reaction else '',
                    'duration' if self.is_duration else '',
                    'command'  if self.is_command  else '',
                    'treasure' if self.is_treasure else '',
                    'victory'  if self.is_victory  else '',
                    *self.additional_types
                ] if typ
            )
        )
