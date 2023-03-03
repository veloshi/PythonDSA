
def toString(List):
    return ''.join(List)
 
def backtrack(s, idx, N,list1):
    if idx == N:
        list1.append(toString(s))
    else:
        for i in range(idx, N + 1):
            s[idx], s[i] = s[i], s[idx]
            backtrack(s, idx + 1, N,list1)
            s[idx], s[i] = s[i], s[idx]
    return list1
 
 
def solve():
    a = "abc"
    b = "ba"
    N = len(a)
    s = list(a)
    list1 = []
    print(backtrack(s, 0, N - 1,list1))
    if b in list1:
        return True
    else:
        return False
    print(list1)
 

print(solve())