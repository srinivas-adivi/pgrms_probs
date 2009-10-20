import prime
def problem27():
	"""http://projecteuler.net/index.php?section=problems&id=27"""
	max_pair = (0,0,0)
	primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
	for a in xrange(-999, 1000):
	    for b in xrange(max(2, 1-a), 1000): # b >= 2, a + b + 1 >= 2
		n, count = 0, 0
		while True:
		    v = n*n + a*n + b
		    v = v <=0 and -v or v
		    if v > primes[-1]:
			prime.primesBelow_fast(v, primes)
			if prime.isprime_fast(v, primes): count = count + 1
			else: break
		    else:
			if not prime.hasFactors(v, primes): count = count + 1
			else: break
		    n = n + 1
		if count > max_pair[2]:
		    max_pair = (a,b,count)
	print max_pair[0] * max_pair[1]
problem27()

