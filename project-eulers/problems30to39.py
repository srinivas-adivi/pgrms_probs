import lib
import prime

def problem30(n):
    """
    >>> problem30(200000)
    443839
    """
    return sum([i for i in range(100, n)\
                    if i == sum(map(lib.call_power, map(lambda x: (x, 5), lib.digits(i))))])
            
def problem31(amount, denominations):
    """ return the number of ways to change any given amount.
         Available coins are also passed as argument to the function.
    >>> import lib
    >>> lib.count_change(10, [1, 5])
    3
    >>> lib.count_change(10, [1, 2])
    6
    >>> lib.count_change(100, [1, 5, 10, 25, 50])
    292
    >>> lib.count_change(200, [1, 2, 5, 10, 20, 50, 100, 200])
    73682
    """
    return lib.count_change(amount, denominations)

def problem32():
    """http://projecteuler.net/index.php?section=problems&id=32
    >>> problem32()
    45228
    """
    set_1to9 = set(['1','2','3','4','5','6','7','8','9'])
    limit_dict = {1: (1001, 5000), 2:(101, 1000)}
    result = {}
    for i in range(2, 100):
        str_i = str(i)
        for j in range(*limit_dict[len(str_i)]):
            product = i*j
            join = str_i+str(j)+ str(product)
            if len(join) == 9 and set(join) == set_1to9:
                result.setdefault(product,[]).append((i,j))
    
    return sum(result.keys())

def problem33(n):
    """http://projecteuler.net/index.php?section=problems&id=33
    >>> numerator, denominator = problem33(2)
    >>> numerator
    8
    >>> denominator
    800
    >>> denominator/numerator
    100
    >>>
    #>>> numerator, denominator = problem33(3)
    #>>> numerator, denominator
    #(3529000151940563851485966406820228553856365890592960149678305265755836649896448673306809449767988263243936600480300689983783821175048754325161255646721091386130091813767906539278271149614446539138572178017378678050718240576773948999564450655267822135426031072732774400000000000000000000000000L, 29416906251134694684587165634107110435272653349147210216900046481871946070445888467614089815853130418865856045692994775556947234020076682861978935209898025543384109520885364633637480096120463950834847756365623772316945572726402784845117998932182335450963361717608416124520631665560781176728953308393809428833133885477475583609588940800000000000000000000000000000000000000L)
    #>>> denominator/numerator
    #8335762251231022414455540008267075418931115082357244869466893691026091030077189L
    """

    fractions = lib.get_fractions(n)
    #trivial = [[(n, d), (dc_n, dc_d)] for [(n,d), (dc_n, dc_d)] in fractions if n==d or (not n%10 and not d%10)]
    non_trivial = [[(n, d), (dc_n, dc_d)] for [(n,d), (dc_n, dc_d)] in fractions if n!=d and n%10 and d%10]
    non_trivial_less_than_one = [[(n,d), (dc_n, dc_d)] for [(n,d), (dc_n, dc_d)] in non_trivial if dc_n<dc_d]
    #print non_trivial_less_than_one
    numerator, denominator = 1, 1
    for [(n,d), (dc_n, dc_d)] in non_trivial_less_than_one:
        numerator, denominator = numerator*dc_n, denominator*dc_d

    return (numerator, denominator)
        
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

def problem35(n):
    """
    >>> problem35(1000000)
    55
    """
    primes = [2, 3]
    prime.primesBelow_fast(50, primes)
    prime.primesBelow_fast(100000, primes)
    prime.primesBelow_fast(n, primes)
    primes = [str(p) for p in primes]

    #to make it fast comment out above lines 
    #uncomment below line 

    #primes = prime.get_primes_from_file()
    
    evens = ['0', '2', '4', '6', '8']
    required_primes = filter(lambda s: not set(s).intersection(evens), primes)
    result = 1
        
    for num in required_primes:
        value = lib.rotation(list(num), required_primes)
        result = result + value

    return result

def problem36(n):
    """ return sum all palindroms in base 10 and 2 below given n
    >>> problem36(1000000)
    872187
    """
    return sum(filter(lib.palindrom_10_2, range(1, n)))

def problem37(n):
    """
    >>> problem37(1000000)
    748317
    """
    primes_below_bilion = [2, 3]
    prime.primesBelow_fast(50, primes_below_bilion)
    prime.primesBelow_fast(100000, primes_below_bilion)
    prime.primesBelow_fast(n, primes_below_bilion)
    
    primes = {}
    for p in primes_below_bilion:
        primes.setdefault(len(str(p)), []).append(str(p))

    #to make it fast comment out above lines 
    #uncomment below line 

    #primes = prime.get_primes_dict_from_file()

    result = [] 
    for L in primes.values():
        call_is_truncatable_prime = lambda n: lib.is_truncatable_prime(n, primes)
        result.extend(filter(call_is_truncatable_prime, L))

    return sum(map(lambda x: int(x), result))

def problem38(n):
    """
    >>> problem38(10000)
    932718654
    """
    result = ''
    for i in xrange(1, n):
        p = lib.pandigital(i) 
        result = p>result and p or result
    
    return int(result)

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
    
def run():
    import doctest
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name == "-v":
            doctest.testmod()
        else:
            test = doctest.DocTestFinder().find(globals()[name])[0]
            runner = doctest.DebugRunner(verbose=True)
            runner.run(test)
    else:
        doctest.testmod()

if __name__ == "__main__":
    run()
