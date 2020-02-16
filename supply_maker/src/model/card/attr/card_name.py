from typing import TYPE_CHECKING

from supply_maker import _where
from supply_maker.src.translation.translatable import Translatable
from supply_maker.src.translation.translate_table import load_translate_table
if TYPE_CHECKING:
    from supply_maker.src.translation import Lang
    from supply_maker.src.translation.translate_table import TranslateTable


class CardName(Translatable):
    _trans_table: 'TranslateTable' = {
        k: v
        for p in (_where / 'res/translate/cards').glob('*.csv')
        for k, v in load_translate_table(p).items()
    }

    def _t(self, lang: 'Lang') -> str:
        cls = type(self)
        return cls._trans_table[self._raw_name][lang]
