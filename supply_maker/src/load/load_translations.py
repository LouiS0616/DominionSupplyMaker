import csv

from ... import where
from ..translation import Lang, TranslateTable

_where = where()


#
def _load_trans(p) -> TranslateTable:
    with open(p, encoding='utf-8', newline='') as fin:
        reader = csv.DictReader(fin)
        ret = {
            row['English']: {
                Lang(k): v or row['English'] for k, v in row.items()
            } for row in reader
        }

    return ret


#
def load_extension_trans() -> TranslateTable:
    return _load_trans(
        _where / 'res/translate/extensions.csv'
    )


def load_card_trans() -> TranslateTable:
    w = _where / 'res/translate/cards'

    ret = {}
    for path in w.glob('*.csv'):
        ret.update(_load_trans(path))

    return ret


def load_term_trans() -> TranslateTable:
    return _load_trans(
        _where / 'res/translate/terms.csv'
    )
