
def problem45():
    t_values = set([n*(n+1)/2 for n in range(185, 2000000)])
    p_values = set([n*(3*n-1)/2 for n in range(165, 1000000)])
    h_values = set([n*(2*n-1) for n in range(143, 1000000)])
    intersection1 = t_values.intersection(p_values)
    return intersection1.intersection(h_values)
    
print problem45()
