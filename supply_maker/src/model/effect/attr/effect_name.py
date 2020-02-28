from typing import TYPE_CHECKING

from supply_maker import _where
from supply_maker.src.translation.translatable import Translatable
from supply_maker.src.translation.translate_table import load_translate_table
if TYPE_CHECKING:
    from supply_maker.src.translation.translate_table import TranslateTable


class EffectName(Translatable):
    _trans_table: 'TranslateTable' = {
        k: v
        for p in (_where / 'res/translate/effects').glob('**/*.csv')
        for k, v in load_translate_table(p).items()
    }

    @property
    def translate_table(self) -> 'TranslateTable':
        cls = type(self)
        return cls._trans_table
