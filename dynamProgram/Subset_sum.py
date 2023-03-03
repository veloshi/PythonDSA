

# Recursive solution 
def recur(arr,sum,n):

    if sum == 0:
        return True
    if n == 0:
        return False
    
    if arr[n-1] <= sum:
        return recur(arr,sum-arr[n-1],n-1) or recur(arr,sum,n-1)
    else:
        return recur(arr,sum,n-1)

arr = [2,3,7,8,10]
sum = 11
if (recur(arr,sum,5) == True):
    print("true")
else:
    print("false")

# def isSubsetSum(set, n, sum):
  
#     # Base Cases
#     if (sum == 0):
#         return True
#     if (n == 0):
#         return False
  
#     # If last element is greater than
#     # sum, then ignore it
#     if (set[n - 1] > sum):
#         return isSubsetSum(set, n - 1, sum)
  
#     # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element
#     # (b) excluding the last element
#     return isSubsetSum(
#         set, n-1, sum) or isSubsetSum(
#         set, n-1, sum-set[n-1])
  
  
# # Driver code
# set = [3, 34, 4, 12, 5, 2]
# sum = 9
# n = len(set)
# if (isSubsetSum(set, n, sum) == True):
#     print("Found a subset with given sum")
# else:
#     print("No subset with given sum")

# #Top Down Approach
# # Recursive solution 
# tab = [[-1 for i in range(2000)] for j in range(2000)]
# def recur(arr,sum,n):
#     if sum == 0:
#         return 1
#     if n <= 0:
#         return 0
#     if (tab[n-1][sum]!=-1):
#         return tab[n][sum]
#     if arr[n-1] <= sum:
#         tab[n-1][sum] = recur(arr,sum-arr[n-1],n-1) or recur(arr,sum,n-1)
#         return tab[n-1][sum]
#     else:
#         tab[n-1][sum] = recur(arr,sum,n-1)
#         return tab[n-1][sum]

# arr = [2,3,7,8,10]
# sum = 11
# recur(arr,sum,5)
# #     print("true")
# # else:
# #     print("false")
def isSubsetSum(set, n, sum):
      
    # The value of subset[i][j] will be 
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset =([[False for i in range(sum + 1)] 
            for i in range(n + 1)])
      
    # If sum is 0, then answer is true 
    for i in range(n + 1):
        subset[i][0] = True
          
    # If sum is not 0 and set is empty, 
    # then answer is false 
    for i in range(1, sum + 1):
         subset[0][i]= False
              
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or 
                                subset[i - 1][j-set[i-1]])
      
    # uncomment this code to print table 
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (subset[i][j], end =" ")
    # print()
    return subset[n][sum]
          
# Driver code
if __name__=='__main__':
    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set)
    if (isSubsetSum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")