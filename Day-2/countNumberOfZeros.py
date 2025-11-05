def countZeros(num,count):
    if num == 0:
        return count
    rem = num%10
    if rem == 0:
        count+=1
    return countZeros(int(num/10),count)


print(countZeros(30204, 0))