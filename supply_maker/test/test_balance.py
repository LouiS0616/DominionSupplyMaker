import collections
import statistics

from tqdm import tqdm

from . import _flush_and_wait
from ..src.model.card_set import Supply
from ..src.model.load import load_cards


# noinspection PyPep8Naming
def test(N=100_000):
    card_set = load_cards()
    counter = collections.Counter()

    for _ in tqdm(range(N), desc='Testing load balance'):
        supply = Supply.frm(card_set)
        assert len(supply) == 10

        # noinspection PyProtectedMember
        counter.update(supply._data)

    values = counter.values()
    print(f'mean:   {statistics.mean  (values):8.2f}')
    print(f'median: {statistics.median(values):8.2f}')
    print(f'stddev: {statistics.pstdev(values):8.2f}')

    (mx_k, mx_v), *_, (mn_k, mn_v) = counter.most_common()
    print(f'max:    {mx_v:5d} {mx_k.name}')
    print(f'min:    {mn_v:5d} {mn_k.name}')

    _flush_and_wait()
