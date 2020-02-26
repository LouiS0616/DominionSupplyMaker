import yaml

from supply_maker import _where
from supply_maker.src.model.card.card import Card
from supply_maker.src.model.card_set.candidates import Candidates


#
def _parse_randomizer(ex, name, attr) -> Card:
    # Basic types and Multi-expansion special types
    universal_types = {
        'Action', 'Treasure', 'Victory',    # 'Curse',
        'Attack', 'Duration', 'Reaction', 'Command',
    }
    return Card.create(
        ex=ex, edition=attr.get('edition', '***'), name=name,
        cost_coin=attr['cost'], need_potion=attr.get('need potion', False),
        **{
            'is_{}'.format(typ.lower()): True for typ in attr['types']
        },
        pile_components=attr.get('pile components', [name])
    )


def load_cards() -> Candidates:
    path = _where / 'res/randomizers'

    #
    s = set()
    for p in path.glob('*.yml'):
        with p.open() as fin:
            data = yaml.load(fin.read(), Loader=yaml.SafeLoader)

        ex = data['ex']
        s |= {
            _parse_randomizer(ex, name, attrs)
            for name, attrs in data['kingdom cards'].items()
        }

    return Candidates(elms=s)
