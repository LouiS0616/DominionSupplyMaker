from typing import TYPE_CHECKING

from ._card_set import CardSet
if TYPE_CHECKING:
    from supply_maker.src.model.constraint.candidate_slimmer import CandidateSlimmer


class Candidates(CardSet):
    def __init__(self, *args, **kwargs):
        self._has_already_slimmed = False
        super().__init__(*args, **kwargs)

    def slim(self, slimmer: 'CandidateSlimmer'):
        new_data = slimmer.slim(self)

        self._data.clear()
        self._data.update(new_data.data)

        self._has_already_slimmed = True

    @property
    def has_already_slimmed(self):
        return self._has_already_slimmed
