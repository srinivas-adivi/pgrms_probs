
def function(I, (n, d)):
    return (I*d+n, d)

def iteration(i, (n,d)):
    if i==1:
	return function(1, (d, n))
    else:
	return iteration(i-1, function(2, (d, n)))

def problem57():
    result = 1
    for i in range(1, 999):
	try:
	    (n, d) = iteration(i, (2, 1))
	except RuntimeError:
	    pass #998
	if len(str(n))>len(str(d)):
	    result = result +1
    return result

print problem57()
