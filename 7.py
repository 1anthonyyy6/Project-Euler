"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
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

num = 2;
prime = [0] * 10001;
prime[0] = num;
num = num + 1;
count = 1;
while (count < 10001):
    if ifPrime(num):
        prime[count] = num;
        count = count + 1;
    num = num + 1;
print("The 10001st prime is ", prime[10000]);