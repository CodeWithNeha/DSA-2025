def splitArrayLargetSum(arr, k):
    start = 0
    end = 0
    for ele in arr:
        if start<ele:
            start=ele
        end += ele

    while(start< end):
        mid = int((start+end)/2)
        sum = 0
        count = 1
        for li in arr:
            if sum+li>mid:
                sum = li
                count+=1
            else:
                sum += li
        if count>k:
            start = mid+1
        else:
            end = mid

    return end


print(splitArrayLargetSum([7,2,5,10,8],2))