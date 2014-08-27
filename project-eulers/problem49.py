import prime
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
prime.primesBelow_fast(103, primes)
def problem49():
    choice = xrange(1489, 3340, 2)
    for n in choice:
	if not prime.hasFactors(n, primes):
	    m1, strn = n+3330, str(n)
	    strm1, setn = str(m1), set(strn)
	    if set(strm1)==setn and not prime.hasFactors(m1, primes):
		m2 = m1+3330
		if set(str(m2))==setn and not prime.hasFactors(m2, primes):
		    return strn+strm1+str(m2)    
print problem49()




