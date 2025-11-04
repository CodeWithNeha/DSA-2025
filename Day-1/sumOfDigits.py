def sumOfDigits(n:int):
    if n <=1:
        return n
    
    rem = n%10
    n = int(n/10)
    return rem + sumOfDigits(n)

print(sumOfDigits(1342))