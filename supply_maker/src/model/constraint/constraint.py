from typing import Callable, List
from typing import TYPE_CHECKING

from supply_maker.src.model.card.evaluate.card_evaluater import has_attr

if TYPE_CHECKING:
    from supply_maker.src.model.card_set.supply import Supply

_SupplyConstraint = Callable[['Supply'], bool]


class SupplyConstraint(_SupplyConstraint):
    def __init__(self, predicate):
        self._predicate = predicate

    def __and__(self, other: 'SupplyConstraint') -> 'SupplyConstraint':
        def _inner(supply: 'Supply') -> bool:
            return self(supply) and other(supply)

        return SupplyConstraint(_inner)

    def __call__(self, supply: 'Supply') -> bool:
        return self._predicate(supply)


#
def comply_with_constraint(
        ac_counts: List[int], **kwargs) -> SupplyConstraint:

    assert len(kwargs) == 1

    def _inner(supply: 'Supply') -> bool:
        return len(
            supply.filter(has_attr(**kwargs))
        ) in ac_counts

    return SupplyConstraint(_inner)
