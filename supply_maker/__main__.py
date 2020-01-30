from .src.model.load import load_cards
from .src.model.card_set import Supply


card_set = load_cards()
while True:
    supply = Supply.frm(card_set)
    supply.setup()

    if supply.is_valid():
        break


print(supply)
print(f'{len(supply)}枚選ばれました')


