import yaml
from yaml import ScalarNode, SequenceNode

from supply_maker import _where
from supply_maker.src.model.card.effect.event import Event
from supply_maker.src.model.card.effect.landmark import Landmark
from supply_maker.src.model.effect_set.effect_set import EffectSet


#
def _flatten(_, node):
    def _inner(n):
        if isinstance(n, ScalarNode):
            yield n
        elif isinstance(n, SequenceNode):
            for e in n.value:
                yield from _inner(e)
        else:
            assert False

    return [v.value for v in _inner(node)]


yaml.add_constructor('!Flatten', _flatten)


#
def _parse_event(ex, name, attr) -> 'Event':
    return Event.create(
        ex=ex, edition=attr.get('edition', '***'),
        name=name, cost=attr['cost'], debt=attr.get('debt', 0)
    )


def _parse_landmark(ex, name, attr) -> 'Landmark':
    return Landmark.create(
        ex=ex, edition=attr.get('edition', '***'),
        name=name
    )


def load_effects() -> 'EffectSet':
    path = _where / 'res/cards'

    #
    s = set()
    for p in path.glob('*.yml'):
        with p.open(encoding='utf-8', newline='') as fin:
            data = yaml.load(fin.read(), Loader=yaml.FullLoader)

        ex = data['ex']
        s |= {
            _parse_event(ex, name, attrs)
            for name, attrs in data.get('events', {}).items()
        }
        s |= {
            _parse_landmark(ex, name, attrs)
            for name, attrs in data.get('landmarks', {}).items()
        }

    if not s:
        raise ValueError(f'Failed to load effect set, check path: {path.resolve()}')

    return EffectSet(elms=s)
