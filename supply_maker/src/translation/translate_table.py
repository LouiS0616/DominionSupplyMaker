import csv
from os import PathLike
from typing import Dict

from .lang import Lang


#
TranslateTable = Dict[str, Dict['Lang', str]]


def load_translate_table(p: 'PathLike') -> TranslateTable:
    with open(p, encoding='utf-8', newline='') as fin:
        reader = csv.DictReader(fin)
        ret = {
            row['English']: {
                Lang(k): v or row['English'] for k, v in row.items()
            } for row in reader
        }

    return ret
