def solve(v,k,idx,ans):
    if len(v) == 1:
        ans = v[0]
        return ans
    idx = ((idx+k)%(len(v)))
    v.remove(v[idx])
    return solve(v,k,idx,ans)

n = 40
k = 7
v = []
for i in range(1,n+1):
    v.append(i)
n =solve(v,k-1,0,ans = 0)
print(n)


a=[5,3,4,2,1]
b=[*a]
a.sort()
print(b)