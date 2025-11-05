def linearSearch(li, target, index, ans):
    if index == len(li):
        return ans
    if li[index] == target:
        ans.append(index)
    return linearSearch(li, target, index+1, ans)

print(linearSearch([3,2,1,4,18,9, 4], 4, 0, []))
