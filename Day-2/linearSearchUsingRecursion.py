def linearSearch(li, target, index):
    if index == len(li):
        return -1
    if li[index] == target:
        return 1
    return linearSearch(li, target, index+1)

print(linearSearch([3,2,1,18,9], 0, 0))
