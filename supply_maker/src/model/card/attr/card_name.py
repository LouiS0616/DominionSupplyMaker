from typing import TYPE_CHECKING

from ....load import load_card_trans
from ....translation.raw_name import RawName
if TYPE_CHECKING:
    from ....translation import Lang


class CardName(RawName):
    _trans_table = None     # loading table should be delayed.

    def _t(self, lang: 'Lang') -> str:
        cls = type(self)
        if cls._trans_table is None:
            cls._trans_table = load_card_trans()

        return cls._trans_table[self._raw_name][lang]
