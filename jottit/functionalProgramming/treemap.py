#! /usr/bin/python
def treemap(f, L):
    """
    >>> treemap(lambda x: x*x, [1, 2, [3, 4], 5])
    [1, 4, [9, 16], 25]
    """
    result = []
    for i in L:
        if isinstance(i, list):
            result.append(treemap(f, i))
        else:
            result.append(f(i))
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
