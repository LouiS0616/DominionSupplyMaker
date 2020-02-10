from typing import TYPE_CHECKING

from ...load import load_extension_trans
from .raw_name import RawName
if TYPE_CHECKING:
    from supply_maker.src.translation import Lang


#
trans_table = load_extension_trans()


class ExtensionName(RawName):
    def _t(self, lang: 'Lang') -> str:
        return trans_table[self._raw_name][lang]
