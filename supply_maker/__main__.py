import argparse
import pathlib
import re

from . import _where
from .make_supply import make_supply


def _init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--constraint', nargs='?',
        help='you can specify a yaml file which control supply balance.',

        type=lambda s: pathlib.Path(s),
        default=(_where / 'res/default_constraints.yml')
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
    from .src.translation import Lang, set_default_lang
    set_default_lang(Lang.JA)
    ###

    parser = _init_parser()
    args = parser.parse_args()

    supply = make_supply(args.constraint)
    supply.print_supply()
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
