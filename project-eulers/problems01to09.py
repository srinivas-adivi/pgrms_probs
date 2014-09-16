import lib

def problem1(num):
    """ return sum of all multiplyer of 3 or 5 below num
    >>> problem1(10)
    23
    >>> problem1(1000)
    233168
    """
    return sum([x for x in range(num)if x%3==0 or x%5==0])

def problem2(num):
    """ return the sum of all the even-valued terms in the sequence which do 
    not exceed num.
    >>> problem2(100)
    188
    >>> problem2(4000000)
    4613732
    """
    a, b, fib = 1, 2, [1, 2]
    while fib[-1] < num: fib.append(fib[-1]+fib[-2])
    return sum(fib[1::3])

def problem3(num):
    """
    >>> problem3(13195)
    29
    >>> problem3(600851475143)
    6857
    """
    primes_dict = lib.prime_factors(num)
    primes = primes_dict.keys()
    primes.sort()
    return primes[-1]

def problem4(start, end):
    """ return largest palindrome made from the product of numbers between 
    start and end
    >>> problem4(10, 100)
    9009
    >>> problem4(100, 1000)
    906609
    """
    L, result = range(start, end), 0
    for i in L:
        for j in L:
            product = i*j
            str1 = str(product)
            result = str1 == str1[::-1] and product > result and product or result
    return result

def problem5(start, end):
    """ return least common multiplyer of all numbers between start and 
    end(include)
    >>> problem5(2, 5)
    60
    >>> problem5(2, 6)
    60
    >>> problem5(2, 20)
    232792560
    """
    L = range(start, end+1)
    result = 1
    for i in L:
        result = lib.lcm(result, i)
    return result

def problem6(n):
    """ return the difference between square of sum of first n natural and sum
    of squares of first n natural numbers
    >>> problem6(10)
    2640
    >>> problem6(100)
    25164150
    """
    sum_numbers = lib.sum_frist_N_numbers(n)
    sum_squres = lib.sum_squares_first_N_numbers(n)
    return (sum_numbers*sum_numbers) - sum_squres

def problem7(n):
    """ return nth prime
    >>> problem7(1)
    2
    >>> problem7(10001)
    104743
    """
    num, count = 1, 0
    while count < n:
        num += 1
        count += num == lib.first_prime_factor(num) and 1 or 0
    return num

def problem8(filename):
    """ return Find the greatest product of five consecutive digits in given
    file which contains the 1000-digit number.
    >>> problem8('problem08.txt')
    40824
    """
    lines, n = open(filename).readlines(), 5
    matrix = [map(lib.convert_int, list(line.strip())) for line in lines]
    return lib.greatest_product_row(matrix, n)

def problem9(n):
    """
    >>> problem9(1000)
    31875000
    """
    return sum([a*b*c for (a, b, c) in lib.right_angle_triangle_sides(1000)])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
