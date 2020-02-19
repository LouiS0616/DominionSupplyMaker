from abc import ABC, abstractmethod
import string
import warnings

from supply_maker.src.translation import get_default_lang
from supply_maker.src.translation.lang import Lang

_ch_set = {
    *string.ascii_letters, *" /'-"
}


class Translatable(ABC):
    def __init__(self, raw_name):
        assert set(raw_name) <= _ch_set, raw_name
        self._raw_name = raw_name

    @abstractmethod
    def _t(self, lang: 'Lang') -> str:
        pass

    def t(self, lang=None) -> str:
        try:
            return self._t(lang or get_default_lang())
        except KeyError:
            warnings.warn(f'Cannot translate; "{self._raw_name}".')
            return self._raw_name

    #
    def __str__(self):
        raise ValueError('call t method to str')

    #
    def __eq__(self, other: 'Translatable'):
        assert type(self) == type(other)
        return self._raw_name == other._raw_name

    def __hash__(self):
        return hash(self._raw_name)
