"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math;
"""
def ifPrime(num):
    int(num);
    flag = False
    if num == 1:
        return False;
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            return False;
        else:
            return True;
"""

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    #Initial array of True  
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    return prime;

def ifCircularPrime(num):   
    digits = digitsCount(num);
    rotated = num;
    if (digits > 1):
        for i in range(1, digits):
            n = rotated;
            x = n % 10;
            rotated = (math.floor(x * (10**(digits-1)) + n / 10));
            if not primes[rotated]:
                return False;
        return True;
    else:
        return True;

def digitsCount(num): 
    count = 0;
    while(num != 0):
        num //= 10;
        count += 1;
    return count;

limit = 1000000;
primes = SieveOfEratosthenes(limit);
cprimes = [True];
count = 0;
for i in range(2, len(primes)):
    if primes[i]:
        if ifCircularPrime(i):
            count += 1;
            cprimes.append(True);
        else: 
            cprimes.append(False);
    else:
        cprimes.append(False);


for i in range(2, len(cprimes)):
    if cprimes[i]:
        print(i);

print("count:", count);





