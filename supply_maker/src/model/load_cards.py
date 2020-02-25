import csv

from supply_maker import _where
from supply_maker.src.model.card.card import Card
from supply_maker.src.model.card_set.candidates import Candidates


def _parse_card(raw: [str]) -> Card:
    # cls and other arguments
    assert 1 + len(raw) == Card.create.__code__.co_argcount, raw

    def _is_t(e):
        return e == '1'

    return Card.create(
        ex=raw[0], edition=raw[1],
        name=raw[2], cost_coin=int(raw[3]), need_potion=_is_t(raw[4]),
        is_action=_is_t(raw[5]), is_attack=_is_t(raw[6]), is_reaction=_is_t(raw[7]),
        is_duration=_is_t(raw[8]), is_command=_is_t(raw[9]),
        is_treasure=_is_t(raw[10]), is_victory=_is_t(raw[11]),
        additional_types=raw[12].split(',')
    )


def load_cards() -> Candidates:
    path = _where / 'res/kingdom_cards'

    #
    s = set()
    for p in path.glob('*.csv'):
        with p.open(encoding='utf-8', newline='') as fin:
            reader = csv.reader(fin)
            next(reader)    # skip header

            s |= {*map(_parse_card, reader)}

    if not s:
        raise ValueError(f'Failed to load card set, check path: {path.resolve()}')

    return Candidates(elms=s)
