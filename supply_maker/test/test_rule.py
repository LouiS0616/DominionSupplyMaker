import sys
from tqdm import tqdm

from .. import _where
from . import _flush_and_wait
from supply_maker.src.model.load_cards import load_cards
from ..src.model.card import Cost
from ..src.model.card.attr.card_name import CardName
from ..src.model.card.evaluate import has_attr
from ..src.model.card_set import Supply
from ..src.model.preparation.role import Role

_card_set = load_cards(_where / 'res/kingdom_cards')


def test():
    _test_young_witch()
    _flush_and_wait()


# noinspection PyProtectedMember,PyPep8Naming
def _test_young_witch():
    # noinspection PyProtectedMember
    def do_once():
        # set includes only 'Young Witch'
        subset = _card_set.filter(has_attr(name=CardName('Young Witch')))
        assert len(subset) == 1

        young_witch = subset.any()

        s = Supply(_frm=(_card_set - subset).choose(9), parent=_card_set)
        s._add_card(young_witch)
        s.setup()

        return s

    N = 100
    for _ in tqdm(range(N), desc='Testing preparation about "young witch"'):
        supply = do_once()

        assert supply.contains(CardName('Young Witch'))
        assert len(supply) == 11

        bane, = [
            card for card in supply._data
            if supply._card_to_role.get(card, Role('')) == Role('Bane')
        ]
        assert bane.cost in (Cost(2), Cost(3))

    print('OK', file=sys.stderr)
