"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
import math
import sys
sys.set_int_max_str_digits(50000)

def pandigital(n):
    num = str(n)
    if "1" in num and "2" in num and "3" in num and "4" in num and "5" in num and "6" in num and "7" in num and "8" in num and "9" in num:
        return True
    return False 

def ifFk(n):
    num = str(n)
    if pandigital(num[0:9:1]) and pandigital(num[len(num):len(num) - 10: -1]):
        return True
    return False

def fibonacci(n) :
    a,b = 1,1
    while n > 2 :
        a,b,n = b, b+a, n-1
    return b

n = 2749
while not ifFk(fibonacci(n)):
    print(n, fibonacci(n))
    n += 1

print(n)