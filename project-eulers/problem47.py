import prime

primes = [2,3,5,7,11,13,17,19,23,29]
prime.primesBelow_fast(int(1000**0.5+1), primes)

def problem47():
    n, count = 6882, 0#2*3*31*37
    while count != 4:
	primeFactors = prime.primeFactors(n, primes)
	if len(primeFactors)==4:
	    count = count+1
	else:
	    count=0
	n=n+1
    return n-4
print problem47()
