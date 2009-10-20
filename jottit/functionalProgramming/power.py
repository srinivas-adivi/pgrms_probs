
def power1(x, n):
    """ Computes the result of x raised to the power of n.
    >>> power1(2, 3)
    8
    >>> power1(3, 2)
    9
    >>> power1(3, 0)
    1
	"""
    str = num_binary(n)
    power1, result = 1, 1
    for i in str[::-1]:
        power1 = power1*x
        result = i=='1' and result*power1 or result
    return result

def num_binary(n):
    binary_str = not n and '0' or ''
    while n:
        binary_str = binary_str+str(n%2)
        n = n>>1
    return binary_str[::-1]

def power2(base, pow):
    """ Computes the result of x raised to the power of n.
    >>> power2(3, 0)
    1
    >>> power2(3, 1)
    3
    >>> power2(3, 2)
    9
	"""
	
    if pow:
        value = pow%2 and base or 1
        return value*power2(base*base, pow>>1)
    else: 
        return 1

def power3(x, n):
    if n:
        return x * power3(x, n-1)    
    else:
        return 1

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
