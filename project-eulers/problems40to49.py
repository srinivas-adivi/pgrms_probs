import lib


def problem40():
    """
    >>> problem40()
    210
    """
    return lib.product(map(lib.nth_digit_fractional, lib.powers10_upto_6))

def problem48(n):
    """ return last 10 digit in sum first n numbers in squence of n power n
    >>> problem48(1000)
    '9110846700'
    """
    return str(lib.sum_powers(n))[-10:]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
