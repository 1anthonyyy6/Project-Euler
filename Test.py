num = "1234567892222222987654321"
def pandigital(n):
    num = str(n)
    if "1" in num and "2" in num and "3" in num and "4" in num and "5" in num and "6" in num and "7" in num and "8" in num and "9" in num:
        return True
    return False 
print(pandigital(num[0:9]), pandigital(num[len(num):len(num) - 10: -1]))
