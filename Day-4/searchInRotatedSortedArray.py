def findPivotElement(li, start, end):
    while(start<=end):
        mid = int((start+end)/2)
        if (mid<end) and li[mid]> li[mid+1]:
            return mid
        elif (mid > start)and li[mid]<li[mid-1]:
            return mid-1
        elif li[start]>=li[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1
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

def searchInRotatedArray(li, start, ele, end):
    pivot = findPivotElement(li, start, end)
    search1 = binarySearch(li, ele, start, pivot)
    if search1 == -1:
        search1 = binarySearch(li, ele, pivot+1, end)

    return search1

print(searchInRotatedArray([4,5,6,7,0,1,2], 0, 0, len([4,5,6,7,0,1,2])-1))
