import yaml

from supply_maker import _where
from supply_maker.src.model.effect.effect import Effect
from supply_maker.src.model.effect_set.effect_set import EffectSet


def _parse_effect(ex, typ, name, attr) -> Effect:
    return Effect.create(
        ex=ex, edition=attr.get('edition', '***'), typ=typ,
        name=name, cost=attr.get('cost', None), debt=attr.get('debt', 0)
    )


def load_effects() -> 'EffectSet':
    path = _where / 'res/randomizers'

    #
    s = set()
    for p in path.glob('*.yml'):
        with p.open(encoding='utf-8', newline='') as fin:
            data = yaml.load(fin.read(), Loader=yaml.SafeLoader)

        ex = data['ex']
        s |= {
            _parse_effect(ex, 'Event', name, attrs)
            for name, attrs in data.get('events', {}).items()
        }
        s |= {
            _parse_effect(ex, 'Landmark', name, attrs)
            for name, attrs in data.get('landmarks', {}).items()
        }

    if not s:
        raise ValueError(f'Failed to load effect set, check path: {path.resolve()}')

    return EffectSet(elms=s)
