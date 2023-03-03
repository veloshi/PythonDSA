# def mergesort(num,low,high):
#     if (low<=high):
#         mid = (high+low)//2
#         mergesort(num,low,mid)
#         mergesort(num,mid+1,high)
#         merge(num,low,mid,high)

# def merge(num,low,mid,high):
#     while i < len(low) and j < len(high):
#         if low[i] <= high[j]:
#             arr[k] = low[i]
#             i += 1
#         else:
#             arr[k] = high[j]
#             j += 1
#             k += 1
 
#         while i < len(low):
#             arr[k] = low[i]
#             i += 1
#             k += 1
 
#         while j < len(high):
#             arr[k] = high[j]
#             j += 1
#             k += 1

# arr = [2,5,1,7]
# low = 0
# high = len(arr)-1
# mergesort(arr,low,high)






































def mergesort(arr):
    inv = 0
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        inv = inv + mergesort(L)
        inv = inv + mergesort(R)
        inv = inv + merge(arr,L,R)
    return inv
def merge(arr,L,R):
    i=j=k=0
    inv = 0
    while i <len(L) and j <len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            inv = inv + len(L)-i
            j = j+1

        k= k+1
    
    while i < len(L):
        arr[k] = L[i]
        i = i+1
        k = k+1 
    while j < len(R):
        arr[k] = R[j]
        j = j+1
        k = k+1
    
    return inv


arr = [1, 20, 6,4]
print(mergesort(arr))