def power(base,pow):
    product = 1
    for i in range(pow):
        product = product*base
    return product

def problem48():
    sum1 = 0
    for i in range(1,1000):
        sum1 = sum1 + power(i,i)
    return str(sum1)[-10:]

print problem48() 

