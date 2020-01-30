import collections
import statistics
import time

from tqdm import tqdm

from ..src.model.card_set import Supply
from ..src.model.load import load_cards


N = 100_000
counter = collections.Counter()

card_set = load_cards()
for _ in tqdm(range(N), desc='Testing load balance'):
    supply = Supply.frm(card_set)
    # noinspection PyProtectedMember
    counter.update(supply._data)


values = counter.values()
print(f'mean:   {statistics.mean  (values):8.2f}')
print(f'median: {statistics.median(values):8.2f}')
print(f'stddev: {statistics.pstdev(values):8.2f}')

(mx_k, mx_v), *_, (mn_k, mn_v) = counter.most_common()
print(f'max:    {mx_v:5d} {mx_k.name}')
print(f'min:    {mn_v:5d} {mn_k.name}')

time.sleep(1)
