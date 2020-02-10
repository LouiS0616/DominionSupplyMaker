import sys


def _flush_and_wait():
    sys.stderr.write('\n')
    sys.stderr.flush()
