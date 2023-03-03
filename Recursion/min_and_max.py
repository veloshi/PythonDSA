
# def minimum(arr,n):
#     if n == 1:
#         return arr[0]
#     return min(arr[n-1],minimum(arr,n-1))


# arr = [777,1,3,33333]
# # n = len(arr)
# print(minimum(arr,n)) 


def minimum(arr,n):
    if n == 1:
        return arr[0]
    return max(arr[n-1],minimum(arr,n-1))


arr = [777,1,3,33333]
n = len(arr)
print(minimum(arr,n)) 