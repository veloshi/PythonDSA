# sequence can be discontinuous.
# def recursiveLCS(X,Y,m,n):
#     if (n==0 or m==0):
#         return 0
#     if X[m-1] == Y[n-1]:
#         return 1+recursiveLCS(X,Y,m-1,n-1)
#     else:
#         return max(recursiveLCS(X,Y,m-1,n),recursiveLCS(X,Y,m,n-1))

# X="AGGTAB"
# Y="GXTXAYB"
# #2 afk
# m = len(X)
# n = len(Y)
# # t = [[-1 for i in range(m+1)] for j in range(n+1)]
# print(recursiveLCS(X,Y,m,n))    
# # print(t)


# def LCS(X,Y,m,n,t):
    
#     if n ==0 or m ==0:
#         return 0
#     if X[m-1] == Y[n-1]:
#         t[m][n] = 1+LCS(X,Y,m-1,n-1,t)
#         return t[m][n]
#     if (t[m][n] != -1):
#         return t[m][n]
#     else:
#         t[m][n] = max (LCS(X,Y,m-1,n,t),LCS(X,Y,m,n-1,t))
#         return t[m][n]

# X="abcd"
# Y="abdc"
# #2 afk
# m = len(X)
# n = len(Y)
# t = [[-1 for i in range(m+1)] for j in range(n+1)]
# print(LCS(X,Y,m,n,t))    
# print(t)

#bottomupApproach
X="AGGTAB"
Y="GXTXAYB"
#2 afk
m = len(X)
n = len(Y)
t = [[-1 for i in range(n+1)] for j in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if (i ==0 or j ==0):
            t[i][j] = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if (X[i-1] == Y[j-1]):
            t[i][j] = 1+t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1]) 

print(t[m][n])





