import lib
import constants

def problem10(num):
    """
    >>> problem10(1000000)
    37550402024
    """
    return sum(lib.primes_below(num))

def problem11(filename):
    """
    >>> problem11('problem11.txt')
    70600674
    """
    n = 4
    lines = open(filename).readlines()
    matrix = [map(lib.convert_int, line.strip().split(' ')) 
                for line in lines]
    d1, d2 = lib.greatest_product_diagonally(matrix, n)
    L = [lib.greatest_product_row(matrix, n), 
        lib.greatest_product_col(matrix, n), d1, d2]
    L.sort()
    return L[-1]

def problem12(n):
    """ return first triangle number to have over n divisors. 
        where triangle number is the sum of first natural numbers.
    >>> problem12(500)
    76576500
    >>> problem12(5)
    28
    """
    divisors, count  = 1, 1
    while divisors < n:
        count += 1
        triangle = lib.sum_frist_N_numbers(count)
        primes_dict = lib.prime_factors(triangle)
        divisors = lib.product(map(lib.increment, primes_dict.values()))
    return triangle

def problem13(filename):
    """ return the first ten digits of the sum of the all digit 
        in given file which contains one-hundred 50-digitnumbers.
    >>> problem13('problem13.txt')
    5537376230
    """
    lines = open(filename).readlines()
    return int(str(sum([int(line.strip()) for line in lines]))[:10])

def problem14(n):
    """ return a number which produces the longest chain of 
        collatz under given n
    >>> problem14(14)
    9
    """
    count, result, d = 1, 1, {1:1}
    odds = range(1, n, 2)
    for i in odds:
        value = lib.collatz_iteration(i, d)
        d[i] = value
        count, result = count > value and (count, result) or (value, i)
    return result

def problem15(n):
    """ return no.of routes from top left corner to bottom right 
        corner in n/n grid 
    >>> problem15(2)
    6
    """
    return lib.ncr(2*n, n)

def problem16(base, pow):
    """
    >>> problem16(2, 1000)
    1366
    """
    value = lib.power(base, pow)
    return sum(lib.digits(value))

def problem17():
    """Return letters would be needed to write all the numbers 
        in words from 1 to 1000"""
    result = len(lib.thousand[0])
    for num in range(1, 1000):
        divident1, remainder1 = divmod(num, 100)
        number_in_words = divident1 and lib.below_20[divident1]+lib.hundred[0] or ''
        
        if remainder1:
            number_in_words = divident1 and number_in_words+'and' or number_in_words
            if remainder1 < 20:
                number_in_words = number_in_words + lib.below_20[remainder1]
            else:
                divident2, remainder2 = divmod(remainder1, 10)
                number_in_words = number_in_words+lib.tys[divident2]
                number_in_words = remainder2 and number_in_words+ lib.below_20[remainder2] or number_in_words

        result = result + len(number_in_words)

    return result

def problem18(triangle):
    '''Find the maximum sum travelling from the top.
    >>> from constants import triangle2, triangle3
    >>> problem18(triangle2)
    1074
    >>> problem18(triangle3)
    7273
    '''
    triangle = triangle.split('\n')
    twodi_list_of_num = [ map(lib.convert_int, words)  
                                for words in map(lambda line: line.split(' '), triangle)]

    return max(reduce(lib.path_sum, twodi_list_of_num)) 

#1stJan 1900 was Monday
def problem19():
    result, starting_day = 0, 0
    Dec31st1900 = lib.find_day_31stDec(1901, starting_day)
    start_of_month = (Dec31st1900+1)%7
    for year in range(1901, 2001):
        value = lib.is_it_leapYear(year)
        for days in map(lambda x: x[value], constants.no_of_days):
            increment = start_of_month==6 and 1 or 0
            result = result + increment
            end_of_month = (days+start_of_month-1)%7
            start_of_month = (end_of_month+1)%7

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
