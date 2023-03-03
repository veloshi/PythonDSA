op1 = ""
op2 = ""
def solve(ip: str,op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op
    op2 = op
    op1 = op + ip[0].capitalize()
    op2 = op2 + ip[0]
    ip = ip[1:]
    solve(ip,op1)
    solve(ip,op2)
    return

ip ="ab"
op = ""
solve(ip,op)