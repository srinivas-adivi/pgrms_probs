def factorial(n):
    if n<=1:
	return 1
    else:
	return n*factorial(n-1)

def problem53():
    result = 0
    for n in range(23, 101):
	for r in range(1, n):
	    (value, L) = n-r < r and (n-r, range(r+1, n+1)) or (r, range(n-r+1, n+1))
	    product1, product2 = 1, 1
	    for i in L:
		product1 = product1*i
	    for j in range(1, value+1):
		product2 = product2*j
	    if 1000000 < (product1/product2):
		result = result + 1

    return result

print problem53()
	
