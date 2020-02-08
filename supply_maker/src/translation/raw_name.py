from abc import ABC, abstractmethod
import string

from .lang import Lang

_ch_set = {
    *string.ascii_letters, ' ', '/', "'",
}


class RawName(ABC):
    def __init__(self, raw_name):
        assert set(raw_name) <= _ch_set
        self._raw_name = raw_name

    @abstractmethod
    def _t(self, lang: 'Lang'):
        pass

    def t(self):
        self._t(Lang.lang())
