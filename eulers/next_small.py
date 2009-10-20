def function(L):
    key, T = L[0], zip(range(len(L), L))
    for(i, n)in T[::-1]:	
	if n < key:
	    return L.pop(i) 
	
def next_small(n):
    """Return next small of given string.
    >>> next_small('312')
    '231'
    >>> next_small('231')
    '213'
    >>> next_small('213')
    '132'
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
