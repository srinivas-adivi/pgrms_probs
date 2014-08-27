def problem32():
    """http://projecteuler.net/index.php?section=problems&id=32"""
    set_1to9 = set(['1','2','3','4','5','6','7','8','9'])
    limit_dict = {1: (1001, 5000), 2:(101, 1000)}
    result = {}
    for i in range(2, 100):
        str_i = str(i)
        for j in range(*limit_dict[len(str_i)]):
            product = i*j
            join = str_i+str(j)+ str(product)
            if len(join) == 9 and set(join) == set_1to9:
                result.setdefault(product,[]).append((i,j))
    
    return sum(result.keys())

print problem32()
