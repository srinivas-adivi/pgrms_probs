def problem56():
    max = 1
    for i in range(1, 100):
	for j in range(1, 100):
	    sum_IpowJ = sum(map(lambda x: int(x), list(str(i**j))))
	    if max < sum_IpowJ:
		max = sum_IpowJ
    return max

print problem56()

