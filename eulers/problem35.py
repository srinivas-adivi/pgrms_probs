
def problem35():
    primes = Primes()
    
    evens = ['0', '2', '4', '6', '8']
    required_primes = filter(lambda s: not set(s).intersection(evens), primes)
    result = 1
        
    for num in required_primes:
        value = rotation(list(num), required_primes)
        result = result + value

    return result
    
def Primes():
    ''' It will give primes below 1000000.'''
    lines = open('primes.txt').readlines()
    primes = []
    for line in lines:
        primes.extend(super_split(line[:-1]))
        
    result = [x for x in primes if x]
    return result

def super_split(s):
    return map(lambda i: s[i:i+8].strip(), range(0, len(s), 8))
               
def rotation(L1, L2):
    index = range(len(L1))
    for i in index:
        last = L1.pop()
        L1.insert(0, last)
        value = ''.join(L1) in L2
        if not value:
            return 0
    return 1

print problem35()
