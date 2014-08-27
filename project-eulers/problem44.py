

def problem44():
    max = 2000
    pent = [n*(3*n-1)/2 for n in xrange(1, 2*max)]
    pdic = dict.fromkeys(pent)
    for j in xrange(0, max):
	for k in xrange(j+1, 2*max-1):
	    p_j = pent[j]
	    p_k = pent[k]
	    p_sum = p_k+p_j
	    p_diff = p_k-p_j
	    #if p_sum in pent[k:k+j] and p_diff in pent[j:k]:
	    if pdic.has_key(p_sum) and pdic.has_key(p_diff):
		return p_diff
print problem44()
