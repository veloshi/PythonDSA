#ip ABC
#op A_B_C

def solve(input,output):
    if(len(input) == 0):
        print(output)
        return                                                                                                                                                                                                                                   
    output1=output
    output2=output
    output1 = output1 + " "+ input[0]
    output2+=input[0]
    input=input[1:]
    solve(input,output1)
    solve(input,output2)
    return

input="abb"                                                                                                                                                                                                                                                             
output=""+input[0]
solve(input[1:],output)
