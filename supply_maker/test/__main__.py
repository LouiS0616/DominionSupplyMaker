import argparse

from . import test_balance
from . import test_constraint
from . import test_rule

from ..src.translation.lang import Lang, set_lang


def _init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'lang', help='indicate lang to be used for logging',
        nargs='?', default='English',
        choices=[ln.value for ln in Lang]
    )

    return parser


def _test_main():
    parser = _init_parser()

    args = parser.parse_args()
    set_lang(Lang(args.lang))

    #
    test_balance.test()
    test_rule.test()
    test_constraint.test()


assert __name__ == '__main__'
_test_main()
