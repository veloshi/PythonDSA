arr = [44]
n = len(arr)
rage = sum(arr)
t =[[False for i in range(rage+1)] for j in range(n+1)]
# print(t)
for i in range(n+1):
    t[i][0] = True
# print(t)
for i in range(1,rage+1):
    t[0][i] = False

    
for i in range(1,n+1):
    for j in range(1,rage+1):
        if arr[i-1]<=j:
            t[i][j] = (t[i-1][j] or t[i-1][j-arr[i-1]])
            print("called")
        if j<arr[i-1]:
            t[i][j] = t[i-1][j]
print(t)
list1 =[]
for j in range((rage//2)+1):
    if t[n][j] == True:
        list1.append(j)
print(list1)
 
mn = 100000
for i in range(len(list1)):
    mn = min(mn,rage-(2*list1[i]))
        
print(mn) 

# ===================
# GFG solution
# #User function Template for python3
# class Solution:
# 	def minDifference(self, arr, n):
# 	    if len(arr) == 1:
# 	        return arr[-1]
# 		rage = sum(arr)
#         t =[[False for i in range(rage+1)] for j in range(n+1)]

#         for i in range(n+1):
#             t[i][0] = True
        
#         for i in range(1,rage+1):
#             t[0][i] = False
            
#         for i in range(1,n+1):
#             for j in range(1,rage+1):
#                 if arr[i-1]<=j:
#                     t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
#                 if arr[i-1]>j:
#                     t[i][j] = t[i-1][j]
        
        
#         list1 = []
#         for j in range(1,(rage//2)+1):
#             if t[n][j] == True:
#                 list1.append(j)
#         mn = 999999999999

#         for i in range(len(list1)):
#             mn = min(mn,rage-(2*list1[i]))
#         return mn