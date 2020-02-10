import argparse
import re

from . import _where
from .make_supply import make_supply
from supply_maker.src.load import load_constraint


def _init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--constraint', nargs='?',
        help='you can specify a yaml file which control supply balance.',

        type=argparse.FileType('r', encoding='utf-8'),
        default=(_where / 'res/constraints.yml').open(encoding='utf-8')
    )
    parser.add_argument(
        '-ss', '--score_sheet', nargs='?',
        help='indicate file to record score. that will be written as CSV encoded by utf-8 with BOM.',

        type=argparse.FileType('a', encoding='utf-8-sig'),
        default=None   # just throw the result away
    )

    return parser


def _main():
    # todo: just for debugging
    from .src.translation.lang import Lang, set_lang
    set_lang(Lang.JP)
    ###

    parser = _init_parser()
    args = parser.parse_args()

    supply = make_supply(
        load_constraint(args.constraint)
    )
    print(supply)
    print(f'{len(supply)}枚選ばれました')
    print()

    if args.score_sheet:
        scores = re.split(
            r'\D+', input('RESULT? (score1 score2 ...) => ')
        )
        print(
            ','.join([*supply.names, *scores]), file=args.score_sheet
        )


_main()
