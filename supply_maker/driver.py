from .src.translation import Lang, set_lang
from .src.translation.name import ExtensionName


set_lang(Lang.JP)

ex = ExtensionName('Seaside')
print(f'---{ex.t()}---')

ex = ExtensionName('Menagerie')
print(f'---{ex.t()}---')
