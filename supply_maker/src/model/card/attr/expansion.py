from typing import TYPE_CHECKING

from supply_maker import _where
from supply_maker.src.translation.translatable import Translatable
from supply_maker.src.translation.translate_table import load_translate_table
if TYPE_CHECKING:
    from supply_maker.src.translation.translate_table import TranslateTable


class Expansion(Translatable):
    _trans_table: 'TranslateTable' = \
            load_translate_table(_where / 'res/translate/expansions.csv')

    def __init__(self, raw_name: str):
        assert raw_name in {
            'Dominion', 'Intrigue', 'Seaside', 'Alchemy', 'Prosperity', 'Cornucopia',
            'Hinterlands', 'DarkAges', 'Guilds', 'Adventures', 'Empires', 'Nocturne',
            'Renaissance',
        }, f'Unknown expansion; "{raw_name}".'

        super().__init__(raw_name)

    @property
    def translate_table(self) -> 'TranslateTable':
        cls = type(self)
        return cls._trans_table

