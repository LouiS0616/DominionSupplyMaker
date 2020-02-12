from typing import TYPE_CHECKING

from supply_maker.src.translation import Translatable
if TYPE_CHECKING:
    from supply_maker.src.translation import Lang, TranslateTable


class ExtensionName(Translatable):
    _trans_table: 'TranslateTable' = None     # loading table should be delayed.

    def _t(self, lang: 'Lang') -> str:
        cls = type(self)
        if cls._trans_table is None:
            from supply_maker.src.load.load_translations import load_extension_trans
            cls._trans_table = load_extension_trans()

        return cls._trans_table[self._raw_name][lang]
