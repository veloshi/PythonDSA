def solve(one,zero,n,op):
    if n == 0:
        print(op)
        return
    op1 = op
    op1 = op1+"1"
    solve(one+1,zero,n-1,op1)

    if (one>zero):
        op2 = op
        op2 = op2+"0"
        solve(one,zero+1,n-1,op2)
        #return
    
n = 3
solve(1,1,n,"")