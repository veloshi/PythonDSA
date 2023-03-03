def helper(arr):
    if len(arr) == 0:
        return    
    k = arr[(len(arr)//2)]
    solve(arr,k)
    return arr

def solve(arr,k):
    if k == 1:
        arr.pop()
        return
    temp = arr.pop()
    solve(arr,k-1)
    arr.append(temp)

arr = [1,2,3,4,5]
print(helper(arr))