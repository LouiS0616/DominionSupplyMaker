from typing import Dict
from typing import TYPE_CHECKING

from .... import get_file_logger
from . import CardSet
from .. import rule
from ..card import Card

if TYPE_CHECKING:
    from ..constraint import SupplyConstraint


# noinspection SpellCheckingInspection
_logger = get_file_logger(
    __name__, form='%(levelname)s | %(message)s'
)


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

    def is_valid(self, constraint: 'SupplyConstraint') -> bool:
        if not self._has_already_set_up:
            self.setup()

        #
        card_names = [card.name for card in self._data]

        if constraint(self):
            _logger.info(f'Accepted: {" ".join(card_names)}')
            return True

        _logger.debug(f'This candidate is ignored: {" ".join(card_names)}')
        return False

    #
    def __str__(self):
        if not self._has_already_set_up:
            raise type(
                'StateError', (ValueError, ), {}
            )('Call both of "setup" and "is_valid" methods before.')

        return '\n'.join(
            '{} {} {}'.format(
                card.cost, card.name,
                '({})'.format(self._card_to_role[card]) if card in self._card_to_role else ''
            )
            for card in self._data
        )
