def productOfDigits(n:int):
    if n <=1:
        return 1
    
    rem = n%10
    n = int(n/10)
    return rem * productOfDigits(n)

print(productOfDigits(1342))