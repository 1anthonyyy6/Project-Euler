"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import math;

def matchDigits(a,b):
    x = sorted(str(a));
    y = sorted(str(b));
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] != y[i]:
                return False;
        return True;
    else:
        return False;

x = 1;
while not (matchDigits(x, 2*x) and matchDigits(x, 3*x) and matchDigits(x, 4*x) and matchDigits(x, 5*x) and matchDigits(x, 6*x)):
    x += 1;

print(x);
