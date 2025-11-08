
def peakBinarySearch(arr, start, end):
    while(start<end):
        mid = int((start + end)/2)
        if arr[mid] >arr[mid+1]:
            end = mid
        else:
            start = mid+1

    return start


def binarySearch(arr, target, start, end):
    while(start<=end):
        mid = int((start + end)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] >target:
            end = mid-1
        else:
            start = mid+1

    return -1


def findInMountainArray(arr, target):
    ele = peakBinarySearch(arr, 0, len(arr)-1)
    search = binarySearch(arr, target, 0, ele)
    search2 = binarySearch(arr, target, ele+1, len(arr)-1)
    print(search, " ,", search2)
findInMountainArray([1,2,3,4,5,3,1], 3)