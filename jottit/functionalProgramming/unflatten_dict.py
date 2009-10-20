#! /usr/bin/python

def unflatten_dict(dict):
    """
    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'c': 4, 'b': {'y': 3, 'x': 2}}
    """
    
    result = {}
    for (key, value) in dict.items():
        if not '.' in key:
            result[key] = value
        else:
#            result.update(unflatten_item((key, value)))
            [(k, v)] = unflatten_item((key, value)).items()
            result.setdefault(k, {}).update(v)
    return result

def unflatten_item((key, value)):
    """
    >>> unflatten_item(('a.x.s', 1))
    {'a': {'x': {'s': 1}}}
    >>> unflatten_item(('a.x', {'s':1}))
    {'a': {'x': {'s': 1}}}
    >>> unflatten_item(('a.x', 2))
    {'a': {'x': 2}}
    """
    [prefix, suffix] = key.rsplit('.',1)
    dir = {suffix: value}

    if '.' in prefix:
        return unflatten_item((prefix, dir))
    else:
        return {prefix: dir}

if __name__ == "__main__":
    import doctest
    doctest.testmod()

