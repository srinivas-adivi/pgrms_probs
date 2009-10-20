
def problem1(num):
    """ return sum of all multiplyer of 3 or 5 below num
    >>> problem1(10)
    23
    """
    return sum([x for x in range(num)if x%3==0 or x%5==0])

def problem2(num):
    """ return the sum of all the even-valued terms in the sequence which do not 
        exceed num.
    >>> problem2(100)
    188
    """
    a, b, fib = 1, 2, [1, 2]
    while fib[-1] < num: fib.append(fib[-1]+fib[-2])
    return sum(L[1::3])

def first_prime_factor(num):
    """ return the first prime factor of given num
    >>> first_prime_factor(24)
    2
    >>> first_prime_factor(25)
    5
    >>> first_prime_factor(19)
    19
    """
    limit = int(num**0.5)
    for i in range(2, limit+1):
        if num%i==0: return i
    return num

def power_and_remainder(num, factor):
    """ return power and remainder as tuple where sum of the remainder and the product 
        of given factor by power time is equal to given num
    >>> power_and_remainder(24, 2)
    (3, 3)
    >>> power_and_remainder(13, 3)
    (0, 13)
    """
    power, remainder = 0, num      
    while not remainder%factor:
        remainder = remainder/factor
        power += 1
    return (power, remainder)
        
                 
def prime_factors(num):
    """ return the dictonary of prime factors of given num contains prime factors as 
        keys and how many times as value
    >>> prime_factors(24)
    {2: 3, 3: 1}
    >>> prime_factors(15)
    {3: 1, 5: 1}
    """
    primes={}
    while num != 1:
        prime = first_prime_factor(num)
        (pow, num) = power_and_remainder(num, prime)
        primes[prime] = pow
    return primes

def problem3(num):
    """
    >>> problem3(13195)
    29
    """
    primes_dict = prime_factors(num)
    primes = primes_dict.keys()
    primes.sort()
    return primes[-1]

def problem4(start, end):
    """ return largest palindrome made from the product of numbers between start and end
    >>> problem4(10, 100)
    9009
    """
    L, result = range(start, end), 0
    for i in L:
        for j in L:
            product = i*j
            str1 = str(product)
            result = str1 == str1[::-1] and product > result and product or result
    return result

def gcd(a, b):
    """ return greatest common divisor of a and b
    >>> gcd(2, 3)
    1
    >>> gcd(0, 6)
    6
    """
    if a == 0: return b
    elif a < b: return gcd(b%a, a)
    else: return gcd(b, a)
        
def lcm(a, b):
    """ return least common multiplyer of a and b
    >>> lcm(2, 3)
    6
    >>> lcm(0, 6)
    0
    """
    gcd_value = gcd(a, b)
    return  (a*b)/gcd_value

def problem5(start, end):
    """ return least common multiplyer of all numbers between start and end(include)
    >>> problem5(2, 5)
    60
    >>> problem5(2, 6)
    60
    """
    L = range(start, end+1)
    result = 1
    for i in L:
        result = lcm(result, i)
    return result

def sum_frist_N_numbers(n):
    """ return sum of first n natural numbers
    >>> sum_frist_N_numbers(7)
    28
    >>> sum_frist_N_numbers(10)
    55
    """
    return n*(n+1)/2

def sum_squares_first_N_numbers(n):
    """ return sum of squares of first n natual numbers
    >>> sum_squares_first_N_numbers(3)
    14
    """
    return n*(n+1)*(2*n+1)/6

def problem6(n):
    """ return the difference between square of sum of first n natural and sum of 
        squares of first n natural numbers
    >>> problem6(10)
    2640
    """
    sum_numbers = sum_frist_N_numbers(n)
    sum_squres = sum_squares_first_N_numbers(n)
    return (sum_numbers*sum_numbers) - sum_squres

def problem7(n):
    """ return nth prime
    >>> problem7(1)
    2
    """
    num, count = 1, 0
    while count < n:
        num += 1
        count += num == first_prime_factor(num) and 1 or 0
    return num

convert_int = lambda x: int(x)

def problem8(filename):
    """ return Find the greatest product of five consecutive digits in given file which
        contains the 1000-digit number.
    >>> problem8('problem8.txt')
    40824
    """
    lines, n = open(filename).readlines(), 5
    matrix = [map(convert_int, list(line.strip())) for line in lines]
    return greatest_product_row(matrix, n)

def right_angle_triangle_sides(n):
    """ return product of pythangorean triplet, (a, b, c) for which a+b+c=1000 and 
        a, b, c should form the right angle triangle i.e sum of squares of a, b is 
        equal to square of c
    >>> right_angle_triangle_sides(1000)
    [(200, 375, 425)]
    >>> right_angle_triangle_sides(120)
    [(20, 48, 52), (24, 45, 51), (30, 40, 50)]
    """
    return [(a, b, n-(a+b)) for a in range(1, n/4+1)
                                for b in range(1, 3*n/4+1)if a*a+b*b==(n-(a+b))**2]
def problem9(n):
    """
    >>> problem9(1000)
    31875000
    """
    return sum([a*b*c for (a, b, c) in right_angle_triangle_sides(1000)])


def problem10(num):
    """
    >>> problem10(1000000)
    37550402023L
    """
    return sum(primes_below(num))

def primes_below(n):
    """ return all prime less than given n
    >>> primes_below(10)
    [1, 2, 3, 5, 7]
    """
    flags = [1]*(n+1)
    primes = [1]
    for i in range(1, n):
        value = i+1
        if flags[value]:
            primes.append(value)
            for j in range(value+value, n+1, value):
                flags[j]=0
    return primes        

def greatest_product_row(matrix, n):
    L = [ product(L[i:i+n]) 
                for L in matrix 
                    for i in range(len(L[:-(n-1)]))]
    L.sort()
    return L[-1]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix[i]))]\
                for i in range(len(matrix))]

def greatest_product_col(matrix, n):
    t = transpose(matrix)
    return greatest_product_row(t, n)

def find_diagonal_list(matrix):
    length = len(matrix)
    L = range(length)
    return [[matrix[i-j][j] for j in range(0, i+1)] for i in L],\
                 [[matrix[i+j][j] for j in range(0, length-i)] for i in L[::-1]] 
    
def greatest_product_diagonally(matrix, n):
    d1, d2 = find_diagonal_list(matrix)
    return greatest_product_row(d1, n), greatest_product_row(d2, n)
    
def problem11(filename):
    """
    >>> problem11('problem11.txt')
    70600674
    """
    n = 4
    lines = open(filename).readlines()
    matrix = [map(convert_int, line.strip().split(' ')) for line in lines]
    d1, d2 = greatest_product_diagonally(matrix, n)
    L = [greatest_product_row(matrix, n), greatest_product_col(matrix, n), d1, d2]
    L.sort()
    return L[-1]

def product(L):
    p = L and 1 or None
    for n in L: p = p*n
    return p

increment = lambda x: x+1

def problem12(n):
    """ return first triangle number to have over n divisors. where triangle number 
        is the sum of first natural numbers.
    >>> problem12(500)
    76576500
    >>> problem12(5)
    28
    """
    divisors, count  = 1, 1
    while divisors < n:
        count += 1
        triangle = sum_frist_N_numbers(count)
        primes_dict = prime_factors(triangle)
        divisors = product(map(increment, primes_dict.values()))
    return triangle

def problem13(filename):
    """ return the first ten digits of the sum of the all digit in given file which 
        contains one-hundred 50-digitnumbers.
    >>> problem13('problem13.txt')
    5537376230L
    """
    lines = open(filename).readlines()
    return int(str(sum([int(line.strip()) for line in lines]))[:10])

def collatz_iteration(n, d={}):
    """ return the length of chain of collatz
    >>> collatz_iteration(13)
    10
    """
    count, value = 0, 0
    while n != 1:
        if d.has_key(n): return count+d[n]
        n = n%2 and 3*n+1 or n>>1
        count +=1
    return count+1
    
def problem14(n):
    """ return a number which produces the longest chain of collatz under given n
    >>> problem14(14)
    9
    """
    count, result, d = 1, 1, {1:1}
    odds = range(1, n, 2)
    for i in odds:
        value = collatz_iteration(i, d)
        d[i] = value
        count, result = count > value and (count, result) or (value, i)
    return result

def ncr(n, r):
    """ return the no.of way that can be choose r things amongs n things
    >>> ncr(4, 2)
    6
    """
    return product(range(-(r+1), -(n+1), -1))/ product(range(1, r+1))

def problem15(n):
    """ return no.of routes from top left corner to bottom right corner in n/n grid 
    >>> problem15(2)
    6
    """
    return ncr(2*n, n)

def power(base, pow):
    """  Computes the result of x raised to the power of n.
    >>> power(3, 3)
    27
    >>> power(0, 3)
    0
    """ 
    if pow:
        value = pow%2 and base or 1
        result = base and value*power(base*base, pow>>1) or 0 
        return result
    else: return 1

def digits(n):
    """ return the list of digits in given n
    >>> digits(372)
    [3, 7, 2]
    """
    return map(convert_int,list(str(n)))

def problem16(base, pow):
    """
    >>> problem16(2, 1000)
    1366
    """
    value = power(base, pow)
    return sum(digits(value))

def factorial(n):
    """
    >>> factoral(5)
    120
    """
    result = product(range(2, n+1)) or 1
    return result
 
def problem20(n):
    """    
    >>> problem20(100)
    648
    """
    value = factorial(n)
    return sum(digits(value))

alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def problem22(filename):
    """
    >>> problem22('problem22.txt')
    871198282
    """
    text = open(filename).read()
    names = text.split(',')
    names.sort()
    names_index = range(len(names))
    return sum([(i+1) * sum([alphabets.index(letter)+1\
                            for letter in names[i].strip('"')])\
                                for i in names_index])

def problem25():
    """
    >>> problem25(1000)
    4782
    """
    fib_nums = [1, 1]
    next_fib = fib_nums[-1]+fib_nums[-2]
    while len(str(next_fib)) < n:
        fib_nums.append(next_fib)
        next_fib = fib_nums[-1] + fib_nums[-2]
    return len(fib_nums)+1
     
def sum_conners_N_spiral(n):
    """ return sum of conners in nth spiral
    >>> sum_conners_N_spiral(5)
    101
    >>> sum_conners_N_spiral(4)
    56
    """
    result, conners = n < 2 and (n%2, []) or (0, range(1, 5))
    for i in conners:
        result += (n-2)*(n-2) + (n-1)*i
    return result

def problem28(n):
    """ return sum of both diagonals in n by n spiral
    >>> problem28(1001)
    669171001
    """
    mod = n%2
    result = sum(map(sum_conners_N_spiral, range(mod, n+1, 2)))
    return result

def problem29(a, b):
    """ return no.of distinct terms in the sequence generated by a power b for 
        2 <= a <= 100 and 2 <= b <= 100?
    >>> problem29(2, 101)
    9183
    """
    L = range(a, b)
    result = len(set([power(x, y) for x in L for y in L]))
    return result

T = lambda x: (x, 5)
call_power = lambda t: power(*t)

def problem30(n):
    """
    >>> problem30(200000)
    443839
    """
    return sum([i for i in range(100, n)\
                    if i == sum(map(call_power, map(T, digits(i))))])
            
def problem34(n):
    """ return sum of all numbers which are equal to the sum of the factorial 
        of their digits.
    >>> problem34(100000)
    40730
    """
    result = 0
    for i in range(3, n):
        digits = map(convert_int, list(str(i)))
        sum_fact_digits = sum(map(factorial, digits))
        if i == sum_fact_digits: result += i
    return result

def is_palindrom(n):
    """ test whether given n is palindrom or not
    >>> is_palindrom(345)
    False
    >>> is_palindrom('303')
    True
    """
    s = str(n)
    return s == s[::-1]

def convert_binary(n):
    """ return binary string of a given n
    >>> convert_binary(3)
    '11'
    >>> convert_binary(10)
    '1010'
    """
    binary = not n and '0' or ''
    while n:
        binary += str(n%2)
        n = n>>1
    return binary[::-1]

palindrom_10_2 = lambda x: is_palindrom(x) and is_palindrom(convert_binary(x))

def problem36(n):
    """ return sum all palindroms in base 10 and 2 below given n
    >>> problem36(1000000)
    872187
    """
    return sum(filter(palindrom_10_2, range(1, n)))

power_10 = lambda i: power(10, i)
powers10_upto_6 = map(power_10, range(7))

def nth_digit_fractional(n):
    if n < 10:
        return n
    else:
        no_digits, key1, key2 = len(str(n)), 0, 0
        for i in range(no_digits):
            value1 = powers10_upto_6[i]*9
            value2 = value1*(i+1)
            if (key1+value2) < n:
                key1 += value1
                key2 += value2
            else: break
        num = key1+(n - key2)/(i+1)
        mod = (n - key2)%(i+1)
        return int(str(num+1)[mod-1])

def problem40():
    """
    >>> problem40()
    210
    """
    return product(map(nth_digit_fractional, powers10_upto_6))

def sum_powers(n):
    """ return sum first n numbers in squence of n power n
    >>> sum_powers(3)
    32
    """
    return sum([power(i, i) for i in range(1, n+1)])

def problem48(n):
    """ return last 10 digit in sum first n numbers in squence of n power n
    >>> problem48(1000)
    '9110846700'
    """
    return str(sum_powers(n))[-10:]

def run():
    import doctest
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
        test = doctest.DocTestFinder().find(globals()[name])[0]
        runner = doctest.DebugRunner(verbose=True)
        runner.run(test)
    else:
        doctest.testmod()
                 
if __name__ == "__main__":
    run()
