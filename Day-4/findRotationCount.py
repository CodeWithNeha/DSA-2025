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


def findRotation(li, start, end):
    pivot = findPivotElement(li, start, end)
    if pivot == -1:
        return 0
    return pivot+1

print(findRotation([4,5,6,7,0,1,2], 0, len([4,5,6,7,0,1,2])-1))