import logging as logging_
from typing import Dict
from typing import TYPE_CHECKING
import warnings

from supply_maker.src.model.preparation.load import load_set_uppers
from ._card_set import CardSet
from .supply_printer import DefaultSupplyPrinter


if TYPE_CHECKING:
    from supply_maker.src.model.card import Card
    from supply_maker.src.model.preparation.role import Role
    from .candidates import Candidates
    from .supply_printer import SupplyPrinter
    from ..constraint.constraint import SupplyConstraint


_default_logger = logging_.getLogger(__name__)
_default_logger.setLevel(logging_.DEBUG)


class Supply(CardSet):
    _set_uppers = load_set_uppers()

    def __init__(self, *,
                 _frm: 'Candidates', parent: 'Candidates',
                 logger: 'logging_.Logger' = None):

        self._has_already_set_up = False
        self._parent = parent
        self._card_to_role: Dict['Card', 'Role'] = {}
        self._notes = []

        self._logger = logger or _default_logger
        super().__init__(elms=_frm.data)

    @staticmethod
    def frm(parent: 'Candidates', *, logger: 'logging_.Logger' = None) -> 'Supply':
        if not parent.has_already_slimmed:
            warnings.warn('candidate is not slimmed')

        return Supply(
            _frm=parent.choose(10), parent=parent, logger=logger
        )

    #
    def _add_card(self, elm: 'Card'):
        self._data |= {elm}

    def setup(self) -> None:
        cls = type(self)
        self._has_already_set_up = True

        for card_name in filter(self.contains, cls._set_uppers):
            candidate = self._parent - self

            cls._set_uppers[card_name](
                add_card=self._add_card,
                candidate=candidate,
                card_to_role=self._card_to_role, notes=self._notes
            )

    #
    def is_valid(self, constraint: 'SupplyConstraint') -> bool:
        if not self._has_already_set_up:
            self.setup()

        #
        card_names = [card.name.t() for card in self.data]
        if constraint(self):
            self._logger.debug(f'Accepted: {" ".join(card_names)}')
            return True
        else:
            self._logger.debug(f'Rejected: {" ".join(card_names)}')
            return False

    #
    def print_supply(self, printer: 'SupplyPrinter' = DefaultSupplyPrinter):
        if not self._has_already_set_up:
            raise type(
                'StateError', (ValueError, ), {}
            )('Call both of "setup" and "is_valid" methods before.')

        printer.print_supply(
            cards=[*self.data], card_to_role=self._card_to_role.copy(), notes=self._notes
        )
