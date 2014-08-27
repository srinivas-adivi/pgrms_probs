#!/usr/bin/python
def problem28():
    sum,sum1= 1,1
    for count in range(2,11,2):
        sum2 = 0
        for count1 in range(1,5):
            temp = count*count1
            sum2 = sum2+sum1+temp
        sum1 = sum1+temp
        sum = sum+sum2
    return sum
print problem28()
