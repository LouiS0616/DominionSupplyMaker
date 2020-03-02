import yaml

from supply_maker import _where
from supply_maker.src.model.card.effect.event import Event
from supply_maker.src.model.card.effect.landmark import Landmark
from supply_maker.src.model.card.effect.effect import Effect
from supply_maker.src.model.effect_set.effect_set import EffectSet


#
def _parse_effect(ex, typ, name, attr) -> 'Effect':
    return Effect.create(
        ex=ex, edition=attr.get('edition', '***'), typ=typ,
        name=name, cost=attr['cost'], debt=attr.get('debt', 0)
    )


def _parse_effect_costless(ex, typ, name, attr) -> 'Effect':
    return Effect.create_costless(
        ex=ex, edition=attr.get('edition', '***'), typ=typ,
        name=name
    )


_effect_create = {
    'event':    _parse_effect,
    'project':  _parse_effect,
    'landmark': _parse_effect_costless,
    #
    'boon':     _parse_effect_costless,
    'hex':      _parse_effect_costless,
    'state':    _parse_effect_costless,
}


#
def load_effects() -> 'EffectSet':
    path = _where / 'res/cards'

    #
    s = set()
    for p in path.glob('*.yml'):
        with p.open(encoding='utf-8', newline='') as fin:
            data = yaml.load(fin.read(), Loader=yaml.SafeLoader)

        ex = data['ex']
        for typ, v in data.get('effect', {}).items():
            effects = {
                _effect_create[typ](ex, typ, name, attrs)
                for name, attrs in v.items()
            }

            if typ in ('event', 'landmark', 'project', ):
                s |= effects

    if not s:
        raise ValueError(f'Failed to load effect set, check path: {path.resolve()}')

    return EffectSet(elms=s)
