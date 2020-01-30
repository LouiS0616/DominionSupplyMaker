import sys
import time


def _flush_and_wait():
    sys.stdout.write('\n')
    sys.stdout.flush()
    time.sleep(1)
