def problem52():
    for n in range(1,1000000):
	n1 = list(str(n))
	n1.sort()
	n2 = list(str(2*n))
	n2.sort()
	n3 = list(str(3*n))
	n3.sort()
	n4 = list(str(4*n))
	n4.sort()
	n5 = list(str(5*n))
	n5.sort()
	n6 = list(str(6*n))
	n6.sort()
	if n1==n2==n3==n4==n5==n6:
	    return n

print problem52()
