from tqdm import tqdm

from . import _flush_and_wait
from ..src.model.load import load_cards
from ..src.model.card_set import Supply
from ..src.model.constraint import comply_with_constraint


card_set = load_cards()


def test(N=100):
    test_single(N)
    test_and(N)
    _flush_and_wait()


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
