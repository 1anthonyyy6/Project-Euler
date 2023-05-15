"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import random;

def pyth(a,b,c):
    if(((a*a + b*b) == (c*c )) & (a < b) & (b < c)):
        return False;
    else: 
        return True;

a = 0; b = 0; c = 0;
while(pyth(a,b,c)):
    a = random.randint(0,1000);
    b = random.randint(0,1000);
    c = 1000 - b - a;
print(a," ",b," ",c,"Product: ", a*b*c);