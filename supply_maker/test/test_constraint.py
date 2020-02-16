import sys
from typing import Callable, List

from tqdm import tqdm

from .. import _where
from . import _flush_and_wait
from supply_maker.src.model.load_cards import load_cards
from ..src.model.card.attr.extension_name import ExtensionName
from ..src.model.card_set import Supply
from ..src.model.constraint import comply_with_constraint, parse_constraint


card_set = load_cards(_where / 'res/kingdom_cards')


def test(N=100):
    test_parse()
    _flush_and_wait()

    test_single(N)
    _flush_and_wait()

    test_and(N)
    _flush_and_wait()


def test_parse():
    print('Testing parse constraint', file=sys.stderr)

    def _inner(src: str, pred: Callable[[List[int]], bool]):
        assert pred(parse_constraint(src))
        print(f'OK -> {src:10s}', file=sys.stderr)

    _inner('*', lambda lst: all(x + 1 == y for x, y in zip(lst, lst[1:])))

    _inner('5',       lambda lst: [5] == lst)
    _inner('0,3-5,7', lambda lst: [0, 3, 4, 5, 7] == lst)
    _inner('*-3',     lambda lst: [0, 1, 2, 3] == lst)

    _inner(
        '0-3,5,7-*',
        lambda lst:
            {0, 1, 2, 3, 5, 7, 8, 9, 10} <= set(lst)
            and set(lst).isdisjoint({4, 6})
    )


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

        print('OK', file=sys.stderr)

    _inner(
        ac_counts=[0, 3, 4, 5], ex=ExtensionName('Alchemy'),
        desc='Testing constraint; 0,3-5 from Alchemy'
    )


def test_and(N):
    # todo: implement
    pass
