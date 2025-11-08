def binarySearch(arr, target, start, end):
    while(start<=end):
        mid = int((start + end)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] >target:
            end = mid-1
        else:
            start = mid+1

    return end

print(binarySearch([2,3,4,5,9,14,16,18], 15, 0, 7))