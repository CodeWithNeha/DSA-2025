def searchInMatrices(arr, target):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if  arr[i][j] == target:
                return i, j
            
    return -1, -1


print(searchInMatrices([[18,9,12],[36,-4,91],[44,33,16]], 91))