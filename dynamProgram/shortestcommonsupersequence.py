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

i,j,s = m,n,""
while(i>0 and j >0):
    if X[i-1] == Y[j-1]:
        s= s + X[i-1]
        i = i-1
        j = j-1
    else:
        if t[i-1][j] >=t[i][j-1]:
            i= i -1
        else:
            j = j-1

print(m+n-t[m][n])

