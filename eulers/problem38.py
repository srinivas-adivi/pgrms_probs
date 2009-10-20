
choice1 = [1,2,3,4,5,6,7,8,9]
choice2 = set(['1','2','3','4','5','6','7','8','9'])

def pandigital(n):
    pandigital = ''.join(map(lambda i: str(i*n), choice1))[:9]
    return set(pandigital) == choice2 and pandigital or ''

def problem38():
    max = ''
    for n in xrange(1, 10000):
	p = pandigital(n) 
	max = p>max and p or max
    
    return max

print problem38()

