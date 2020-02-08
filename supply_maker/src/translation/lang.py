from enum import Enum


class Lang(Enum):
    EN = ENG = 'English'
    JP = JPG = 'Japanese'

    #
    _lang: 'Lang' = EN  # default

    @classmethod
    def lang(cls) -> 'Lang':
        return cls._lang

    @classmethod
    def set_lang(cls, lang: 'Lang'):
        cls._lang = lang
