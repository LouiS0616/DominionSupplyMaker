from .src.model.card.attr.expansion_name import ExpansionName
from .src.translation import Lang, set_lang


from .src.model.card.attr.card_name import CardName

set_lang(Lang.JP)
print(CardName('Moat').t())
