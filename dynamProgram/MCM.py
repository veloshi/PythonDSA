# #MCM is matrix chain multiplication. consider we have given and arr of size n 
# # arr = [40,20,30,10,30] n = 5
# # no. of matrix = n -1 = 4
# # A1,A2,A3,A4 = matrix 
# # dimensions to be calculated like A1 = arr[i-1]*arr[i]
# # i will be 1 and j will be len(n) 
# import sys
# def solve(arr,i,j):
    
#     if (i>=j):
#         return 0
#     mini = sys.maxsize
#     for k in range(i,j):
#         tempans = solve(arr,i,k) + solve(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
        
#         if tempans<mini:
#             mini = tempans

#     return mini

# arr = [1, 2, 3, 4, 3]
# print(solve(arr,1,len(arr)-1))

#Memoized code.
import sys

def solve(arr,i,j):
    t = [[-1 for i in range(10)] for i in range(10)]
    # print(t)
    if (i>=j):
        return 0
    if(t[i][j] != -1):
        return t[i][j]
    
    mini = sys.maxsize

    for k in range(i,j):
        tempans = solve(arr,i,k) + solve(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
        
        if tempans<mini:
            mini = tempans
            t[i][j] = mini
    return t[i][j]

arr = [1, 2, 3, 4, 3]
print(solve(arr,1,len(arr)-1))