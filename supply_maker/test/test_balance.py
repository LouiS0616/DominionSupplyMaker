import collections
import statistics

from tqdm import tqdm

from .. import _where, get_file_logger
from . import _flush_and_wait
from ..src.model.card_set import Supply
from supply_maker.src.load import load_cards


_logger = get_file_logger(
    __name__, form='%(message)s'
)


# noinspection PyPep8Naming
def test(N=100_000):
    card_set = load_cards(_where / 'res/kingdom_cards')
    counter = collections.Counter()

    for _ in tqdm(range(N), desc='Testing load balance'):
        supply = Supply.frm(card_set)
        assert len(supply) == 10

        # noinspection PyProtectedMember
        counter.update(supply._data)

    #
    values = counter.values()
    print(f'mean:   {statistics.mean  (values):8.2f}')
    print(f'median: {statistics.median(values):8.2f}')
    print(f'stddev: {statistics.pstdev(values):8.2f}')

    (mx_k, mx_v), *_, (mn_k, mn_v) = counter.most_common()
    print(f'max:    {mx_v:5d} {mx_k.name}')
    print(f'min:    {mn_v:5d} {mn_k.name}')

    #
    for k, v in counter.most_common():
        _logger.debug(f'{k}: {v}')

    #
    _flush_and_wait()
