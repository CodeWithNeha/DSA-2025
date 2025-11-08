def peakBinarySearch(arr, start, end):
    while(start<end):
        mid = int((start + end)/2)
        if arr[mid] >arr[mid+1]:
            end = mid
        else:
            start = mid+1

    return start

print(peakBinarySearch([0,1,0],0, 2))