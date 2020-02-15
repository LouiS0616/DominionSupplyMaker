from typing import Callable, Dict, List
from supply_maker.src.model.card.attr import CardName


#
SupplySetUpper = Callable[
    [
        Callable[['Card'], None],   # for adding extra card
        'CardSet',                  # candidate
        Dict['Card', 'Role'],       # card to role
        List[str]                   # notes
    ], None
]


#
def register_set_upper(name: str):
    def _decorator(func):
        _inner: SupplySetUpper

        def _inner(*, add_card, candidate, card_to_role, notes):
            return func(add_card, candidate, card_to_role, notes)

        _set_uppers[CardName(name)] = _inner
        return _inner

    return _decorator


_set_uppers = {}
