from abc import ABC, abstractmethod
import string

from supply_maker.src.translation import Lang, get_lang

_ch_set = {
    *string.ascii_letters, ' ', '/', "'",
}


class RawName(ABC):
    def __init__(self, raw_name):
        assert set(raw_name) <= _ch_set
        self._raw_name = raw_name

    @abstractmethod
    def _t(self, lang: 'Lang') -> str:
        pass

    def t(self) -> str:
        return self._t(get_lang())
