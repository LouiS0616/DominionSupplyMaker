import re
from typing import Callable, List
from typing import TYPE_CHECKING

from ..card.evaluate import has_attr

if TYPE_CHECKING:
    from ..card_set import Supply

_SupplyConstraint = Callable[['Supply'], bool]


class SupplyConstraint(_SupplyConstraint):
    def __init__(self, pred):
        self._pred = pred

    def __call__(self, supply: 'Supply') -> bool:
        return self._pred(supply)


#
def _range_closed(start, end) -> List[int]:
    assert start < end
    assert 0 <= start and end <= 10

    return [e for e in range(start, end+1)]


def _parse_constraint(src: List[str]) -> List[int]:
    if not src:
        return []

    s, *rest = src

    if re.fullmatch(r'[0-9]|10', s):
        return [int(s)] + _parse_constraint(rest)

    assert re.fullmatch(r'([0-9]|10|\*)-([0-9]|10|\*)', s)
    start, end = s.split('-')
    start =  0 if start == '*' else int(start)
    end   = 10 if end   == '*' else int(end)

    return _range_closed(start, end) + _parse_constraint(rest)


def parse_constraint(src: str) -> List[int]:
    if not src:
        raise ValueError

    if src == '*':
        return _range_closed(0, 10)

    return _parse_constraint(src.split(','))


#
def comply_with_constraint(
        ac_counts: List[int], **kwargs) -> SupplyConstraint:

    assert len(kwargs) == 1

    def _inner(supply: 'Supply') -> bool:
        return len(supply.filter(
            has_attr(**kwargs)
        )) in ac_counts

    return SupplyConstraint(_inner)
