
def next_big(n):
    """Return next small of given string.
    >>> next_big('')
    >>> next_big('0')
    >>> next_big('31')
    >>> next_big('13')
    '31'
    >>> next_big('231')
    '312'
    >>> next_big('3421')
    '4123'
    >>> next_big('53146')
    '53164'
    >>> next_big('53412')
    '53421'
    """
    length = len(n)
    index = xrange(length-1, 0, -1)
    for i in index:
	cur, prev = n[i], n[i-1]
	if cur > prev:
	    slice1, slice2 = list(n[:i-1]), list(n[i-1:])
	    key1, T = prev, zip(xrange(length-i+1), slice2)
	    for (j, n) in T[::-1]:
		if n>key1:
		    key = slice2.pop(j)
		    break
	    slice2.sort()
	    slice2.insert(0, key)
	    return ''.join(slice1+slice2)

def next_small(n):
    """Return next small of given string.
    >>> next_small('')
    >>> next_small('0')
    >>> next_small('13')
    >>> next_small('31')
    '13'
    >>> next_small('321')
    '312'
    >>> next_small('4213')
    '4132'
    >>> next_small('53416')
    '53164'
    >>> next_small('53412')
    '53241'
    """
    length = len(n)
    index = xrange(length-1, 0, -1)
    for i in index:
	cur, prev = n[i], n[i-1]
	if cur < prev:
	    slice1, slice2 = list(n[:i-1]), list(n[i-1:])
	    key1, T = prev, zip(xrange(length-i+1), slice2)
	    for (j, n) in T[::-1]:
		if n<key1:
		    key = slice2.pop(j)
		    break
	    slice2.sort(reverse=True)
	    slice2.insert(0, key)
	    return ''.join(slice1+slice2)

def permutation(n):
    """Return permutation list for a given string.
    >>> permutation('321')
    ['321', '312', '231', '213', '132', '123']
    """
    p_list = [n]
    nextSmall = next_small(n)
    while nextSmall and nextSmall[0]!='0':
	p_list.append(nextSmall)
	nextSmall = next_small(nextSmall)
    
    return p_list

if __name__== "__main__":
    import doctest
    doctest.testmod()
