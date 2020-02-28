from dataclasses import dataclass
from typing import Union


CostType = Union['Cost', 'Costless']


#
@dataclass(order=True, frozen=True)
class Cost:
    cost_coin: int
    need_potion: bool = False
    debt: int = 0

    def __str__(self):
        return '{coin}{potion}{debt}'.format(
            coin=self.cost_coin,
            potion='+P' if self.need_potion else '',
            debt=f'<{self.debt}>' if self.debt else ''
        )


class Costless:
    def __eq__(self, other):
        return isinstance(other, Costless)

    def __lt__(self, other):
        return isinstance(other, Cost)
