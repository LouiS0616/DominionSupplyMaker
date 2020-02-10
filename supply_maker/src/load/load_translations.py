import csv

from ... import where
from ..translation import Lang, TranslateTable

_where = where()


#
def _load_extension_trans(fin) -> TranslateTable:
    reader = csv.DictReader(fin)
    return {
        row['English']: {
            Lang(k): v or row['English'] for k, v in row.items()
        } for row in reader
    }


def load_extension_trans() -> TranslateTable:
    with open(_where / 'res/translate/extensions.csv', encoding='utf-8', newline='') as fin:
        ret = _load_extension_trans(fin)

    return ret


#
def _load_card_trans(fin) -> TranslateTable:
    reader = csv.DictReader(fin)
    return {
        row['English']: {
            Lang(k): v or row['English']  for k, v in row.items()
        } for row in reader
    }


def load_card_trans() -> TranslateTable:
    w = _where / 'res/translate/cards'

    ret = {}
    for path in w.glob('*.csv'):
        with open(path, encoding='utf-8', newline='') as fin:
            ret.update(_load_card_trans(fin))

    return ret

