import csv
from typing import Dict

from ... import where
from ..translation import Lang

TranslateTable = Dict[str, Dict[Lang, str]]
_where = where()


#
def _load_extension_trans(fin) -> TranslateTable:
    reader = csv.DictReader(fin)
    return {
        row['English']: {
            Lang(k): v for k, v in row.items()
        } for row in reader
    }


def load_extension_trans() -> TranslateTable:
    with open(_where / 'res/translate/extensions.csv', encoding='utf-8') as fin:
        ret = _load_extension_trans(fin)

    return ret
