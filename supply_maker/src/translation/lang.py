from enum import Enum


class Lang(Enum):
    EN = ENG = 'English'
    JP = JPG = 'Japanese'


#
_lang: 'Lang' = Lang.EN  # default


def get_lang() -> 'Lang':
    return _lang


def set_lang(lang: 'Lang'):
    global _lang
    _lang = lang

