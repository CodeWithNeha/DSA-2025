def stepCount(num, count):
    if num == 0:
        return count
    
    if num % 2==0:
        return stepCount(int(num/2),count+1 )
    return stepCount(num-1, count+1)

print(stepCount(14, 0))
