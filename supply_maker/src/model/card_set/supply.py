from typing import Dict

from . import CardSet
from .. import rule
from ..card import Card


class Supply(CardSet):
    def __init__(self, *args, parent: CardSet, _frm: CardSet = None, **kwargs):
        self._has_already_set_up = False
        self._parent = parent
        self._card_to_role: Dict[Card, str] = {}

        if _frm is None:
            super().__init__(*args, **kwargs)
        else:
            assert not args
            assert not kwargs

            super().__init__(_frm=_frm)

    @classmethod
    def frm(cls, parent: CardSet) -> 'Supply':
        return Supply(
            _frm=parent.choose(10), parent=parent
        )

    def setup(self) -> None:
        self._has_already_set_up = True

        set_uppers = rule.load(self)
        for set_upper in set_uppers:
            set_upper(
                self, self._parent - self, self._card_to_role, []
            )

    def is_valid(self) -> bool:
        if not self._has_already_set_up:
            self.setup()

        # todo: implement
        return True

    #
    def __str__(self):
        return '\n'.join(
            '{} {} {}'.format(
                card.cost, card.name,
                '({})'.format(self._card_to_role[card]) if card in self._card_to_role else ''
            )
            for card in self._data
        )