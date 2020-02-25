from typing import TYPE_CHECKING

from supply_maker import _where
from supply_maker.src.translation.translatable import Translatable
from supply_maker.src.translation.translate_table import load_translate_table
if TYPE_CHECKING:
    from supply_maker.src.translation.translate_table import TranslateTable


class Role(Translatable):
    _trans_table: 'TranslateTable' = \
            load_translate_table(_where / 'res/translate/terms.csv')

    @property
    def translate_table(self) -> 'TranslateTable':
        cls = type(self)
        return cls._trans_table
