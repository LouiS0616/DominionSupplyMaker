from dataclasses import dataclass


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
