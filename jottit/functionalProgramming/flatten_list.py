#! /usr/bin/python

def flatten_list(a, result=None):
    """Flattens a nested list.
    >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result
if __name__== "__main__":
    import doctest
    doctest.testmod()

