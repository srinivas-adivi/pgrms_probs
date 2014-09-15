import lib

def problem30(n):
    """
    >>> problem30(200000)
    443839
    """
    return sum([i for i in range(100, n)\
                    if i == sum(map(lib.call_power, map(lambda x: (x, 5), lib.digits(i))))])
            
def problem34(n):
    """ return sum of all numbers which are equal to the sum of the factorial 
        of their digits.
    >>> problem34(100000)
    40730
    """
    result = 0
    for i in range(3, n):
        digits = map(lib.convert_int, list(str(i)))
        sum_fact_digits = sum(map(lib.factorial, digits))
        if i == sum_fact_digits: result += i
    return result

def problem36(n):
    """ return sum all palindroms in base 10 and 2 below given n
    >>> problem36(1000000)
    872187
    """
    return sum(filter(lib.palindrom_10_2, range(1, n)))

def problem39(m, n):
    """
    >>> problem39(800, 900)
    840
    """
    result = [len(lib.right_angle_triangle_sides(i)) for i in range(m, n)]
    temp = result[:]
    temp.sort()
    index = result.index(temp[-1])+m
    count = result.count(temp[-1])
    return index
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
