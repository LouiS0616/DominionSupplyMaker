import sys
from typing import List

from tqdm import tqdm

from . import _flush_and_wait
from ..src.model.load import load_cards
from ..src.model.card_set import Supply
from ..src.model.constraint import comply_with_constraint, parse_constraint


card_set = load_cards()


def test(N=100):
    test_parse()
    _flush_and_wait()

    test_single(N)
    _flush_and_wait()

    test_and(N)
    _flush_and_wait()


def test_parse():
    print('Testing parse constraint', file=sys.stderr)

    def _inner(src: str, dst: List[int]):
        assert parse_constraint(src) == dst
        print(f'OK -> {src:10s} => {dst}')

    _inner('*', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    _inner('5', [5])
    _inner('0,3-5,7', [0, 3, 4, 5, 7])
    _inner('0-3,5,7-*', [0, 1, 2, 3, 5, 7, 8, 9, 10])
    _inner('*-3', [0, 1, 2, 3])


def test_single(N):
    # noinspection PyProtectedMember
    def _inner(*, ac_counts, desc, **kwargs):
        for _ in tqdm(range(N), desc=desc):
            supply = Supply.frm(card_set)
            supply.setup()

            (attr, value), = kwargs.items()
            constraint = comply_with_constraint(
                ac_counts=ac_counts, **kwargs
            )
            num_of_compatible_cards = sum(
                getattr(card, attr) == value
                for card in supply._data
            )

            assert constraint(supply) == (num_of_compatible_cards in ac_counts)

        print('OK')

    _inner(
        ac_counts=[0, 3, 4, 5], ex='錬金術',
        desc='Testing constraint; 0,3-5 from Alchemy'
    )


def test_and(N):
    # todo: implement
    pass
