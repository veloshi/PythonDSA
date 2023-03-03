def findPath( m, n):
     # code here
        visited = [[False for _ in range(n)] for _ in range(n)]
        res = []
        osf = ""
        i = 0
        j = 0
        if m[i][j] == 0:
            return res
        solve(m, n, i, j, osf, visited, res)
        return res

def solve(m, n, i, j, osf, visited, res):
    if i == n-1 and j == n-1:
        res.append(osf)
        return
    
    # is it safe to moving further
    if not (isSafe(i, j, n, visited)):
        return
    
    visited[i][j] = True
    # check right
    if (isSafe(i, j+1, n, visited)) and m[i][j+1] == 1:
        solve(m, n, i, j+1, osf+"R", visited, res)
    # check left
    if (isSafe(i, j-1, n, visited)) and m[i][j-1] == 1:
        solve(m, n, i, j-1, osf+"L", visited, res)
    # check bottom
    if (isSafe(i+1, j, n, visited)) and m[i+1][j] == 1:
        solve(m, n, i+1, j, osf+"D", visited, res)
    # check up
    if (isSafe(i-1, j, n, visited)) and m[i-1][j] == 1:
        solve(m, n, i-1, j, osf+"U", visited, res)
    
    visited[i][j] = False
        
 
def isSafe(i, j, n, visited):
    if i >= 0 and j >= 0 and i < n and j < n and visited[i][j] == False:
        return True
    return False

m = [[1, 0, 0, 0],
[1, 1, 0, 1],
[1, 1, 0, 0],
[1, 1, 1, 1]]
n = len(m)
print(findPath(m,n))

