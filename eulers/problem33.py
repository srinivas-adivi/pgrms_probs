
def make_dict():
    dict, key, value = {}, 1, 10
    for n in range(11, 100):
	if n%10:
	    dict.setdefault(str(key), []).append(n)
	else:
	    key = key+1
	    value = value*key
    return dict

def problem33():
    """http://projecteuler.net/index.php?section=problems&id=33"""
    from decimal import Decimal
    dict, result = make_dict(), []
    for L in dict.values():
	for n in L:
	    str_n = str(n)
	    set_n, [tens, ones] = set(str_n), list(str_n)
	    for d in dict[ones]:
		set_d = set(str(d))
		intersection = set_n.intersection(set_d)
		if intersection:
		    difference_n = list(set_n.difference(set_d))
		    difference_d = list(set_d.difference(set_n))
		    if difference_n and difference_d:
			fraction1=Decimal(difference_n[0])/Decimal(difference_d[0])
			fraction2=Decimal(n)/Decimal(d)
			if fraction1 == fraction2:
			    result.append((n, d))

    return result

print problem33()
