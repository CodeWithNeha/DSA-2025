def revNum(num):
    rev = 0
    while(num!=0):
        rem = num%10
        print(rem)
        rev = rev*10+ rem
        num = int(num/10)

    return rev

print(revNum(123))
