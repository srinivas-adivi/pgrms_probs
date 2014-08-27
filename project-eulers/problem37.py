def super_split(s):
    return map(lambda i: s[i:i+8].strip(), range(0, len(s), 8))

def Primes():
    ''' It will give primes below 1000000.'''
    lines = open('primes.txt').readlines()
    primes, result = [], {}
    for line in lines:
        primes.extend(super_split(line[:-1]))
        
    for p in primes:
        if p:
            result.setdefault(len(p), []).append(p)
            
    return result

primes_below_bilion = Primes()

def truncate_left_right(length, n):
    for i in range(1, length):
        if not n[i:] in primes_below_bilion[length-i]:
            return False
    return True
                
def truncate_right_left(length, n):
    for i in range(1, length):
        if not n[:-i] in primes_below_bilion[length-i]:
            return False
    return True

def is_truncatable_prime(n):
    length = len(n)
    if length > 1:
        if(truncate_left_right(length, n) and truncate_right_left(length, n)):
            return True
    return False
    
def problem37():
    result_list = []
    for L in primes_below_bilion.values():
        result_list.extend(filter(is_truncatable_prime, L))
    print sum(map(lambda x: int(x), result_list))

problem37()
