"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 
"""
def ifPrime(num):
    flag = False
    if num == 1:
        print(num, "is not a prime number")
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

x = [];
c = 0;
num = 600851475143;
for i in range(1, num):
    if(((num % i) == 0) & ifPrime(num)):
        c = c + 1;
        x.append(i);
print(x[x.__len__]);