import collections
import statistics
import sys

from tqdm import tqdm

from .. import _where, get_file_logger
from . import _flush_and_wait
from ..src.model.card_set import Supply
from supply_maker.src.model.load_cards import load_cards


_logger = get_file_logger(
    __name__, form='%(message)s'
)


# noinspection PyPep8Naming,PyProtectedMember
def test(N=100_000):
    card_set = load_cards(_where / 'res/kingdom_cards')
    counter = collections.Counter()

    for _ in tqdm(range(N), desc='Testing load balance'):
        supply = Supply.frm(card_set)
        assert len(supply._data) == 10

        counter.update(supply._data)

    #
    values = counter.values()
    print(f'mean:   {statistics.mean  (values):8.2f}', file=sys.stderr)
    print(f'median: {statistics.median(values):8.2f}', file=sys.stderr)
    print(f'stddev: {statistics.pstdev(values):8.2f}', file=sys.stderr)

    (mx_k, mx_v), *_, (mn_k, mn_v) = counter.most_common()
    print(f'max:    {mx_v:5d} {mx_k.name.t()}', file=sys.stderr)
    print(f'min:    {mn_v:5d} {mn_k.name.t()}', file=sys.stderr)

    #
    for k, v in counter.most_common():
        _logger.debug(f'{k.name.t()}: {v}')

    #
    _flush_and_wait()
