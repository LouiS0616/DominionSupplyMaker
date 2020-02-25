import csv

from supply_maker import _where
from supply_maker.src.model.effect.effect import Effect
from supply_maker.src.model.effect_set.effect_candidate import EffectCandidate


def _parse_effect(raw: [str]) -> Effect:
    # cls and other arguments
    assert 1 + len(raw) == Effect.create.__code__.co_argcount, raw

    return Effect.create(
        ex=raw[0], edition=raw[1], typ=raw[2],
        name=raw[3], cost=raw[4]
    )


def load_effects() -> 'EffectCandidate':
    path = _where / 'res/effects'

    #
    s = set()
    for p in path.glob('**/*.csv'):
        with p.open(encoding='utf-8', newline='') as fin:
            reader = csv.reader(fin)
            next(reader)    # skip header

            s |= {*map(_parse_effect, reader)}

    if not s:
        raise ValueError(f'Failed to load effect set, check path: {path.resolve()}')

    return EffectCandidate(elms=s)
