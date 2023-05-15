"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
def dSum(n): #take the digital sum
    sum = 0
    while n!=0:
        sum+=n%10
        n //= 10
    return sum

def sqrt(n): #squareroot with 100 digit precision
    a=5 * n
    b=5
    limit = 10**(101)
    while b < limit:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100 
            b = (b-b%10)*10 + b%10

    root = int(str(b)[:100])
    return root

sum = 0;
for i in range(1, 101):
    if i not in [1,4,9,16,25,36,49,64,81,100]:
        sum += dSum(sqrt(i));

print(sum);



