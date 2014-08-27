from library import prime_factors, power, right_angle_triangle_sides

prime_power= lambda (x, y): zip([x]*(y+1), range(y+1))
call_power = lambda x: power(*x)

def product_lists(a, b):
    '''
    >>> L1 = [1, 2]
    >>> L2 = [1, 2, 3]
    >>> product_lists(L1, L2)
    [1, 2, 3, 2, 4, 6]
    '''
    return [i*j for i in a for j in b]

def factors(n):
    """
    >>> factors(1)
    [1]
    >>> factors(3)
    [1, 3]
    >>> factors(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    """
    primes = prime_factors(n)
    value = [map(call_power, prime_power(tuple))for tuple in primes.items()]
    result = value and value[0] or [1]
    for i in value[1:]:
        result = product_lists(result, i)
    result.sort()
    return result

def is_amicable(n):
    """
    >>> is_amicable(220)
    True
    >>> is_amicable(284)
    True
    >>> is_amicable(6)
    False
    """
    a = sum(factors(n)[:-1])
    b = sum(factors(a)[:-1])
    return n == b and n != a

def problem21(m, n):
    """
    >>> problem21(2, 10000)
    31626
    """
    return sum([i for i in range(m, n) if is_amicable(i)])

def problem39(m, n):
    """
    >>> problem39(800, 900)
    840
    """
    result = [len(right_angle_triangle_sides(i)) for i in range(m, n)]
    temp = result[:]
    temp.sort()
    index = result.index(temp[-1])+m
    count = result.count(temp[-1])
    return index
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()    
