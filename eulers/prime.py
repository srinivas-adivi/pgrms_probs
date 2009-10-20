	
def primesBelow(n):
    ''' return a list of primes below given n.
    >>> primesBelow(4)
    [2, 3]
    >>> primesBelow(3)
    [2]
    >>> primesBelow(2)
    []
    '''
    primes = [2]
    for m in xrange(3, n, 2):
	if not hasFactors(m, primes):
	    primes.append(m)

    return n!=2 and primes or []

def primeFactors(N, primesBelowN):
    ''' return a the prime composite factor as dict which contains primes as keys and powers as values.
    >>> primeFactors(31)
    {31: 1}
    >>> primeFactors(32)
    {2: 5}
    >>> primeFactors(40)
    {2: 3, 5: 1}
    '''
    primes = primesBelowN and primesBelowN or primesBelow(int(n**0.5+1))
    primefactors = {}
    for p in primes:
	while not N%p:
	    N = N/p
	    primefactors[p] = primefactors.get(p, 0)+1
	if N==1: break
    if N != 1:
	primefactors[N] = 1
    
    return primefactors

def nthprime(N):
    ''' return nth prime where n as given.
    >>> nthprime(1)
    2
    >>> nthprime(10)
    29
    >>> nthprime(10001)
    104743
    '''
    primes, NoOfPirmes, n = [2, 3], 2, 3
    while NoOfPirmes < N:
	n = n+2
	if not hasFactors(n, primesList):
	    primes.append(n)
	    NoOfPirmes = NoOfPirmes+1
    
    return N==1 and 2 or primes[-1]

def hasFactors(n, primes=[]):
    ''' return either True or False'''
    choice = primes and primes or xrange(3, n, 2)
    for m in choice:
	if m*m>n or not n%m: break
    if choice:
	return not m*m>n and True or False
    else:
	return False

def isprime(n):
    ''' return either True or False'''
    return (n%2 or n==2) and not hasFactors(n) or False

def isprime_fast(n, primes):
    for p in primes:
	if not n%p: return False
    return True

def primesBelow_fast(n, primes=[2,3]):
    ''' update the given know primes list upto given n'''
    maxPrime = primes[-1]
    limit = int(n**0.5+1)
    choice = maxPrime<limit and xrange(maxPrime+2, limit, 2) or []
    for c in choice:
	if isprime_fast(c, primes):
	    primes.append(c)
	    maxPrime = c
    limitedPrimes = primes[:]
    for c in xrange(maxPrime+2, n, 2):
	if isprime_fast(c, limitedPrimes):
	    primes.append(c)

def updatePrimes(primes, limit):
    maxPrime = primes[-1]
    if limit<maxPrime:
	return primes
    else:
        for n in xrange(maxPrime+2, limit, 2):
	    if isprime_fast(n, primes):
		primes.append(n)

if __name__== "__main__":
    '''
    primes = [2, 3]
    primesBelow_fast(10, primes)
    print len(primes)
    print primes
    primesBelow_fast(20, primes)
    print primes
    '''
