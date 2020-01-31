import re
from typing import List

#
# Typically supply consists of ten kind of kingdom-cards,
# but some card exists which can change the number into more than 10: e.g. "Young Witch".
#
# So it's not good idea to always convert * to 0 or 10, the up-limit is unknown.
#

_END = 32


def _range_closed(start, end) -> List[int]:
    assert 0 <= start < end <= _END
    return [e for e in range(start, end+1)]


def _parse_constraint(src: List[str]) -> List[int]:
    if not src:
        return []

    s, *rest = src

    number = r'0|[1-9][0-9]*'
    if re.fullmatch(number, s):
        return [int(s)] + _parse_constraint(rest)

    assert re.fullmatch(fr'({number}|\*)-({number}|\*)', s)
    start, end = s.split('-')
    start =    0 if start == '*' else int(start)
    end   = _END if end   == '*' else int(end)

    return _range_closed(start, end) + _parse_constraint(rest)


def parse_constraint(src: str) -> List[int]:
    if not src:
        raise ValueError

    if src == '*':
        return _range_closed(0, 10)

    return _parse_constraint(src.split(','))
