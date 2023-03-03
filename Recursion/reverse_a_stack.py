def reverse(s):
    #base condition
    if len(s)==1:
        return 
    temp = s.pop()
    #Hypothesis
    reverse(s)
    #induction
    solve(s,temp)
    return s
def solve(arr,k):
    #base condition
    if len(arr) == 0:
        arr.append(k)
        return
    val = arr.pop()
    #Hypothesis
    solve(arr,k)
    #induction
    arr.append(val)


s = [1,2,3,4,5]
print(reverse(s))