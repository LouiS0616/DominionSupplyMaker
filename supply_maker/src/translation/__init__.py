from .lang import Lang


#
_default_lang = None


def get_default_lang() -> 'Lang':
    global _default_lang

    if _default_lang is None:
        _default_lang = Lang.EN

    return _default_lang


def set_default_lang(new_lang: 'Lang') -> None:
    global _default_lang
    _default_lang = new_lang
