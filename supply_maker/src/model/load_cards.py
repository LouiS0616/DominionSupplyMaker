import csv
from os import PathLike
from pathlib import Path
from typing import List

from supply_maker.src.model.card import Card
from supply_maker.src.model.card.attr import ExtensionName
from supply_maker.src.model.card_set import CardSet


def _ex_name(stem: str) -> str:
    return stem


def _parse_card(stem: str, raw: [str]) -> Card:
    # cls, ex and other arguments
    assert 2 + len(raw) == Card.create.__code__.co_argcount

    def _is_t(e):
        return e == '1'

    return Card.create(
        ex=_ex_name(stem), name=raw[0], cost_coin=int(raw[1]), need_potion=_is_t(raw[2]),
        is_action=_is_t(raw[3]), is_attack=_is_t(raw[4]), is_reaction=_is_t(raw[5]), is_duration=_is_t(raw[6]),
        is_treasure=_is_t(raw[7]), is_victory=_is_t(raw[8])
    )


def load_cards(
        path: PathLike, *,
        extensions_never_used: List['ExtensionName'] = None) -> CardSet:

    path = Path(path)

    if extensions_never_used is None:
        extensions_never_used = []

    #
    s = set()
    for p in path.glob('*.csv'):
        if ExtensionName(p.stem) in extensions_never_used:
            continue

        with p.open(encoding='utf-8', newline='') as fin:
            reader = csv.reader(fin)
            next(reader)    # skip header

            s |= {
                _parse_card(p.stem, line) for line in reader
            }

    if not s:
        raise ValueError(f'Failed to load card set, check path: {path.resolve()}')

    return CardSet(elms=s)
