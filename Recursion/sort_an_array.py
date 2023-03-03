
def insert(arr, temp):
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return
        
    val = arr[len(arr) - 1]
    arr.pop()
    insert(arr, temp)
    arr.append(val)

def sort( arr):
    if len(arr) == 1:
        return
    temp = arr[len(arr) - 1]
    arr.pop()
    sort(arr)
    insert(arr, temp)
    return arr

arr = [2, 3, 5, 4]
print(sort(arr))