def solve(ip,op):
    if len(ip) == 0:
        print(op)
        return
    op1=op
    op2=op
    if ip[0].isalpha():
        op1 = op1+ip[0].upper()
        op2 = op2+ip[0].lower()
        ip = ip[1:]
        solve(ip,op1)
        solve(ip,op2)
        return
    else:
        op1 = op1+ip[0]
        ip = ip[1:]
        solve(ip,op1)
        return
    
ip = "a1b2"
op = ""
solve(ip,op)