import re
from typing import List


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
