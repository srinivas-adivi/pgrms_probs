#! /usr/bin/python

def flatten_dict(a, key=[], result=None):
    """
    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if result is None:
        result = {}

    for x in a:
        k = key+[x]
        if isinstance(a[x], dict):
            flatten_dict(a[x], k, result)
        else:
            result['.'.join(k)] = a[x]

    return result
if __name__ == "__main__":
    import doctest
    doctest.testmod()
