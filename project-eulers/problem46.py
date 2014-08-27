import prime

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
squares = dict.fromkeys((x*x for x in xrange(1, 10000)), 1)
prime.primesBelow_fast(10000, primes)
for x in xrange(35, 10000, 2):
    if not prime.isprime(x):
        is_goldbach = 0
        for p in primes[1:]:
            if p >= x: break
            if squares.has_key((x - p)/2):
                is_goldbach = 1
                break
        if not is_goldbach:
            print x
            break

