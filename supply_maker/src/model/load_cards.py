import yaml
from yaml.nodes import ScalarNode, SequenceNode

from supply_maker import _where
from supply_maker.src.model.card.gainable.card import Card
from supply_maker.src.model.card_set.candidates import Candidates


#
def _parse_card(ex, name, attr, randomizer) -> Card:
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


#
def load_cards() -> Candidates:
    path = _where / 'res/cards'

    #
    s = set()
    for p in path.glob('*.yml'):
        with p.open() as fin:
            data = yaml.load(fin.read(), Loader=yaml.SafeLoader)

        ex = data['ex']
        cards = data['card']
        s |= {
            _parse_card(ex, name, attrs, randomizer=True)
            for name, attrs in cards['randomizer'].items()
        }

        # just load cards which is not randomizer
        _ = {
            _parse_card(ex, name, attrs, randomizer=False)
            for name, attrs in {
                **cards.get('basic supply', {}),
                **cards.get('part of pile', {}),
                **cards.get('non-supply', {})
            }.items()
        }

    return Candidates(elms=s)
