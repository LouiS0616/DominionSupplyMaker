from .src.model.card.attr.extension_name import ExtensionName
from .src.translation import Lang, set_lang


set_lang(Lang.JP)

ex = ExtensionName('Seaside')
print(f'---{ex.t()}---')

ex = ExtensionName('Menagerie')
print(f'---{ex.t()}---')
