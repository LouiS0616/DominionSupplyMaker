import yaml

from supply_maker import _where
from supply_maker.src.model.card.gainable.card import Card
from supply_maker.src.model.card_set.candidates import Candidates


#
def _parse_card(ex, name, attr, randomizer) -> Card:
    # Basic types and Multi-expansion special types
    universal_types = {
        'Action', 'Treasure', 'Victory', 'Curse',
        'Attack', 'Duration', 'Reaction', 'Command',
    }
    return Card.create(
        ex=ex, edition=attr.get('edition', '***'), name=name,
        cost_coin=attr['cost'],
        need_potion=attr.get('need potion', False),
        debt=attr.get('debt', 0),
        cost_mark=attr.get('cost mark', ''),
        **{
            'is_{}'.format(typ.lower()): True for typ in attr['types']
        },
        randomizer=randomizer,
        pile_cards=attr.get('pile cards', [name]),
        related_cards=attr.get('related cards', [])
    )


def load_cards() -> Candidates:
    path = _where / 'res/cards'

    #
    s = set()
    for p in path.glob('*.yml'):
        with p.open() as fin:
            data = yaml.load(fin.read(), Loader=yaml.SafeLoader)

        ex = data['ex']
        s |= {
            _parse_card(ex, name, attrs, randomizer=True)
            for name, attrs in data['kingdom cards'].items()
        }

        _ = {
            _parse_card(ex, name, attrs, randomizer=False)
            for name, attrs in data.get('basic supply', {}).items()
        }
        _ = {
            _parse_card(ex, name, attrs, randomizer=False)
            for name, attrs in data.get('non-supply', {}).items()
        }
        _ = {
            _parse_card(ex, name, attrs, randomizer=False)
            for name, attrs in data.get('other kingdom', {}).items()
        }

    return Candidates(elms=s)
