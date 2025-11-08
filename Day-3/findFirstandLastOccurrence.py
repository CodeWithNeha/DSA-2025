
def binarySearch(arr, target, start, end, startindex):
    ans = -1
    while(start<=end):
        mid = int((start + end)/2)
        if arr[mid] == target:
            ans = mid
            if startindex:
                end = mid-1
            else:
                start = mid+1
        elif arr[mid] >target:
            end = mid-1
        else:
            start = mid+1

    return ans
def searchRange( nums, target):
    print(binarySearch(nums, target, 0, len(nums)-1, True))
    print(binarySearch(nums, target, 0, len(nums)-1, False))





searchRange([5,7,7,8,8,10],7)


