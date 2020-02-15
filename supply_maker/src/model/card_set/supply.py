from typing import Dict
from typing import TYPE_CHECKING

from .... import get_file_logger
from . import CardSet
from .. import preparation
from ..card import Card

if TYPE_CHECKING:
    from ..constraint import SupplyConstraint
    from supply_maker.src.model.preparation.role import Role


# noinspection SpellCheckingInspection
_logger = get_file_logger(
    __name__, form='%(levelname)s | %(message)s'
)


class Supply(CardSet):
    def __init__(self, *, _frm: CardSet, parent: CardSet):
        self._has_already_set_up = False
        self._parent = parent
        self._card_to_role: Dict[Card, 'Role'] = {}

        super().__init__(elms=_frm.data)

    @classmethod
    def frm(cls, parent: CardSet) -> 'Supply':
        return Supply(
            _frm=parent.choose(10), parent=parent
        )

    def add(self, elm: 'Card'):
        self._data |= {elm}

    #
    def setup(self) -> None:
        self._has_already_set_up = True

        set_uppers = preparation.load(self)
        for set_upper in set_uppers:
            set_upper(
                self, self._parent - self, self._card_to_role, []
            )

    def is_valid(self, constraint: 'SupplyConstraint') -> bool:
        if not self._has_already_set_up:
            self.setup()

        #
        card_names = [card.name.t() for card in self._data]

        if constraint(self):
            _logger.debug(f'Accepted: {" ".join(card_names)}')
            return True

        _logger.debug(f'Rejected: {" ".join(card_names)}')
        return False

    #
    def __str__(self):
        if not self._has_already_set_up:
            raise type(
                'StateError', (ValueError, ), {}
            )('Call both of "setup" and "is_valid" methods before.')

        return '\n'.join(
            '{} {} {}'.format(
                card.cost, card.name.t(),
                '({})'.format(self._card_to_role[card].t()) if card in self._card_to_role else ''
            )
            for card in self._data
        )
