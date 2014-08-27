def problem55():
    result = 0
    for i in range(11, 10001):
	reverse_str_i = int(str(i)[::-1]) 
	value = i == reverse_str_i and i+reverse_str_i or i
	for j in range(1, 50):
	    reverse_str = str(value)[::-1]
	    reverse_int = int(reverse_str)
	    if value == reverse_int:
		break
	    else:
		value = value+reverse_int
	else:
	    result = result+1
    
    return result

print problem55()
