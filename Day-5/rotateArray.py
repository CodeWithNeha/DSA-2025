def reverseArray(arr, start, end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1

arr = [1,2,3,4,5,6,7]
k = 3
k = int(k%len(arr))
reverseArray(arr, 0, len(arr)-1-k)
reverseArray(arr, len(arr)-k, len(arr)-1)
reverseArray(arr, 0, len(arr)-1)
print(arr)

