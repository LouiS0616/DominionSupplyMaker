from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Cost:
    cost_coin: int
    need_potion: bool = False

    def __str__(self):
        return '{coin}{potion:2s}'.format(
            coin=self.cost_coin,
            potion='+P' if self.need_potion else ''
        )
