#!/usr/bin/python

from math import factorial
#number of digits
n = 10
#index ends at zero, must account for this
permN = 10**6 - 1
#digits to work with, ie [0,9] 
digits = range(n)
#string being built
a = ''
#index of digits element
i = 0
while permN:
    count = factorial(len(digits)-1)*(i+1)
    if(count > permN):
        a += str(digits[i])
        digits.pop(i)
        permN = permN - last
        i = 0
    else:
        i += 1
    last = count

#tag on the remaining elements in increasing order
while digits:
    a += str(digits.pop(0))
    
print a