import sys
from tqdm import tqdm

from .. import _where
from . import _flush_and_wait
from supply_maker.src.load import load_cards
from ..src.model.card import Cost
from ..src.model.card.attr.card_name import CardName
from ..src.model.card.evaluate import has_attr
from ..src.model.card_set import Supply


_card_set = load_cards(_where / 'res/kingdom_cards')


def test():
    _test_young_witch()
    _flush_and_wait()


# noinspection PyProtectedMember,PyPep8Naming
def _test_young_witch():
    def do_once():
        # set includes only 'young witch'
        subset = _card_set.filter(has_attr(name=CardName('Young Witch')))
        assert len(subset) == 1

        s = Supply(_frm=(_card_set - subset).choose(9), parent=_card_set)
        s.add(subset.any())

        s.setup()
        return s

    N = 100
    for _ in tqdm(range(N), desc='Testing rule about "young witch"'):
        supply = do_once()

        assert supply.contains(CardName('Young Witch'))
        assert len(supply) == 11

        bane, = [
            card for card in supply._data
            if supply._card_to_role.get(card) == '災い'
        ]
        assert bane.cost in (Cost(2), Cost(3))

    print('OK', file=sys.stderr)



