import constants


def find_day_31stDec(year, starting_day):
    '''
    >>> find_day_31stDec(2009, 3)
    3
    '''
    value = is_it_leapYear(year) and 1 or 0
    total_days = sum(map(lambda x : x[value], constants.no_of_days))
    
    remainder = (total_days+starting_day-1)%7
    
    return remainder
            
def is_it_leapYear(year):
    ''' 
    >>> is_it_leapYear(2009)
    False
    >>> is_it_leapYear(2008)
    True
    '''
    div1, mod1 = divmod(year, 100)
    div2, mod2 = mod1 and divmod(year, 4) or divmod(div1, 4)

    return not mod2

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
    
def product(L):
    p = L and 1 or None
    for n in L: p = p*n
    return p

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
    
def ncr(n, r):
    """ return the no.of way that can be choose r things amongs n things
    >>> ncr(4, 2)
    6
    """
    return product(range(-(r+1), -(n+1), -1))/ product(range(1, r+1))

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

def factorial(n):
    """
    >>> factorial(5)
    120
    """
    result = product(range(2, n+1)) or 1
    return result
 
def sum_conners_N_spiral(n):
    """ return sum of conners in nth spiral
    >>> sum_conners_N_spiral(5)
    76
    >>> sum_conners_N_spiral(3)
    24
    """
    result, conners = n < 2 and (n%2, []) or (0, range(1, 5))
    for i in conners:
        result += (n-2)*(n-2) + (n-1)*i
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

def sum_powers(n):
    """ return sum first n numbers in squence of n power n
    >>> sum_powers(3)
    32
    """
    return sum([power(i, i) for i in range(1, n+1)])

def path_sum(L1, L2):
    '''
    >>> path_sum([1], [2, 3])
    [3, 4]
    >>> path_sum([3, 4], [4, 5, 6])
    [7, 9, 10]
    >>> path_sum([7, 9, 10], [7, 8, 9, 10])
    [14, 17, 19, 20]
    '''
    L1, L2 = zip(L1, L2[:-1]), zip(L1, L2[1:])
    L1.append(L2[-1])
    L2.insert(0, L1[0])
    return map(lambda ((x1, x2),(y1, y2)): max(x1+x2, y1+y2), zip(L1, L2))
    
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
                 
convert_int = lambda x: int(x)
increment = lambda x: x+1
decrement = lambda x: x-1
call_power = lambda t: power(*t)
power_10 = lambda i: power(10, i)
powers10_upto_6 = map(power_10, range(7))


if __name__ == "__main__":
    run()
