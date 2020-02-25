import functools
import operator


def combination(n, k):
    """
    >>> combination(0, 0)
    1
    >>> combination(0, 1)
    0
    >>> combination(10, 2)
    45
    """

    if k > n:
        return 0

    k = min(n-k, k)
    numerator = functools.reduce(
        operator.mul, range(n, n-k, -1), 1
    )
    denominator = functools.reduce(
        operator.mul, range(1, k + 1), 1
    )

    return numerator // denominator


#
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
