from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from supply_maker.src.model.card.evaluate.card_evaluater import CardEvaluator
    from supply_maker.src.model.card_set.candidates import Candidates


#
class CandidateSlimmer:
    def __init__(self, predicate_false: 'CardEvaluator'):
        # return True if card is unnecessary
        self._predicate_false = predicate_false

    def slim(self, candidate: 'Candidates') -> 'Candidates':
        return candidate.filter(
            lambda card: not self._predicate_false(card)
        )
