import csv
import re

from supply_maker import _where
from supply_maker.src.model.card.card import Card
from supply_maker.src.model.card_set.candidates import Candidates


def _ex_name(stem: str) -> str:
    m = re.fullmatch(r'ex\d{2}_(?P<name>.+)', stem)
    assert m, stem

    return m.group('name')


def _parse_card(stem: str, raw: [str]) -> Card:
    # cls, ex and other arguments
    assert 2 + len(raw) == Card.create.__code__.co_argcount, raw

    def _is_t(e):
        return e == '1'

    return Card.create(
        ex=_ex_name(stem), name=raw[0], cost_coin=int(raw[1]), need_potion=_is_t(raw[2]),
        is_action=_is_t(raw[3]), is_attack=_is_t(raw[4]), is_reaction=_is_t(raw[5]), is_duration=_is_t(raw[6]),
        is_treasure=_is_t(raw[7]), is_victory=_is_t(raw[8])
    )


def load_cards() -> Candidates:
    path = _where / 'res/kingdom_cards'

    #
    s = set()
    for p in path.glob('*.csv'):
        with p.open(encoding='utf-8', newline='') as fin:
            reader = csv.reader(fin)
            next(reader)    # skip header

            s |= {
                _parse_card(p.stem, line) for line in reader
            }

    if not s:
        raise ValueError(f'Failed to load card set, check path: {path.resolve()}')

    return Candidates(elms=s)
