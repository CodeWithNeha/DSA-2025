def arrayTest(li, index):
    if index == len(li)-1:
        return 0
    if li[index] >li[index+1]:
        return 1
    return arrayTest(li, index+1)

print(arrayTest([1,2,4,3,9,12],0))