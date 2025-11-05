
def revNum(num, rev):
    if num==0:
        return rev
    rem = num%10
    rev = rev*10+rem
    return revNum(int(num/10),rev)


print(revNum(123, 0))
