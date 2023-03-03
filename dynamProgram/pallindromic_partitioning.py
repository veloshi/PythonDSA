import sys
def isPalindrome(s):
 
     if s == s[::-1]:
        
        return True
     else:
        return False
 
 
# Driver code
# s = "malayalam"
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")

# def solve(s,i,j):

#     if i>=j:

#         return 0
#     if isPalindrome(s[i:j+1]) == True:
#         return 0
#     mn = sys.maxsize
#     for k in range(i,j):
#         temp = 1+solve(s,i,k) + solve(s,k+1,j) 

#         if temp <mn:
#             mn = temp
#     return mn 

# s = "abac"
# n = len(s)
# m = solve(s,0,n-1)
# print(m)

#memoized version
# def solve(s,i,j):
#     t = [[ -1 for i in range(10)] for j in range(10)]
#     if i>=j:

#         return 0
#     if isPalindrome(s[i:j+1]) == True:
#         return 0
#     if(t[i][j] != -1):
#         return t[i][j]
#     mn = sys.maxsize
#     for k in range(i,j):
#         temp = 1+solve(s,i,k) + solve(s,k+1,j) 

#         if temp <mn:
#             mn = temp
#     t[i][j] =mn
#     return t[i][j]

# s = "abac"
# n = len(s)
# m = solve(s,0,n-1)
# print(m)

#optimized memoized version
def solve(s,i,j):
    t = [[ -1 for i in range(10)] for j in range(10)]
    if i>=j:

        return 0
    if isPalindrome(s[i:j+1]) == True:
        return 0

    mn = sys.maxsize
    for k in range(i,j):                                     
            if(t[i][k] != -1):
                left = t[i][k]
            else:
                left =solve(s,i,k)
            if(t[k+1][j] != -1):
                right = t[i][k]
            else:
                right =solve(s,k+1,j)

            temp = 1+ left + right
            if temp <mn:
                mn = temp
    t[i][j] =mn
    return t[i][j]

s = "geek"
n = len(s)
m = solve(s,0,n-1)
print(m)