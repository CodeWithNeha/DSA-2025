def binarySearch(n: int, start:int, end: int, ele: int) -> int:
    if start>end:
        return -1
    mid = int((start + end)/2)
    if ele>n[mid]:
        start = mid + 1
    elif ele<n[mid]:
        end = mid-1
    else:
        return mid
    return binarySearch(n,start,end,ele)


n = [-1,0,3,5,9,12]
target = 9

print(binarySearch(n, 0, len(n)-1, target))