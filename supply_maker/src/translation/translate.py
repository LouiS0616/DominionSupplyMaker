from typing import Dict
from .lang import Lang


TranslateTable = Dict[str, Dict['Lang', str]]

#
_default_lang: 'Lang' = Lang.EN


def get_default_lang() -> 'Lang':
    return _default_lang


def set_default_lang(new_lang: 'Lang') -> None:
    global _default_lang
    _default_lang = new_lang
