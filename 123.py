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

sieve = SieveOfEratosthenes(1000000)
def nthPrime(n):
    count = 0
    i = 1
    while (count <= n):
        if sieve[i]:
            count += 1
        i += 1
    return i

min = 10**10

def findR(n):
    p = nthPrime(n)
    r = ((p - 1)**n + (p + 1)**n)%(p*p) 
    return r

n = 0
while(findR(n) <= min):
    print(n,findR(n))
    n += 1

print(n)