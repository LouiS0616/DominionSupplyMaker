from typing import TYPE_CHECKING

from ....translation.translatable import Translatable
if TYPE_CHECKING:
    from ....translation import Lang


class CardName(Translatable):
    _trans_table = None     # loading table should be delayed.

    def _t(self, lang: 'Lang') -> str:
        cls = type(self)
        if cls._trans_table is None:
            from ....load.load_translations import load_card_trans
            cls._trans_table = load_card_trans()

        return cls._trans_table[self._raw_name][lang]
