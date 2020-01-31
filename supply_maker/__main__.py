import argparse

from . import _where
from .src.model.load import load_cards
from .src.model.card_set import Supply


def _init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--constraint', nargs='?',
        help='you can specify a yaml file which control supply balance.',

        type=argparse.FileType('r', encoding='utf-8'),
        default=(_where / 'res/constraints.yml').open(encoding='utf-8')
    )

    return parser


def _main():
    parser = _init_parser()
    args = parser.parse_args()
    # print(args.constraint)


_main()

card_set = load_cards()
while True:
    supply = Supply.frm(card_set)
    supply.setup()

    if supply.is_valid():
        break


print(supply)
print(f'{len(supply)}枚選ばれました')


