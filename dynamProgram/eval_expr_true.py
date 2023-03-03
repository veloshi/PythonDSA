from collections import defaultdict
dict = defaultdict()
def solve(s,i,j,istrue):

    if(i>j):
        return 0
    if(i==j):
        if(istrue==True):
            return s[i]=='T'
        else:
            return s[i]=='F'
    temp = str(i)
    temp =temp+" "
    temp = temp + str(j)
    temp =temp+" "
    temp= temp + str(istrue)
    if dict.get('temp') != None:
        return dict[temp]

    ans=0
    for k in range (i+1,j,2):

        lt=solve(s,i,k-1,True)
        lf=solve(s,i,k-1,False)
        rt=solve(s,k+1,j,True)
        rf=solve(s,k+1,j,False)
        if(s[k]=='&'):
            if(istrue==True):
                ans=ans+lt*rt
            else:
                ans=ans+lf*rf+lf*rt+lt*rf
        elif(s[k]=='|'):

                if(istrue==True):
                    ans+=(lt*rt)+(lt*rf)+(lf*rt)
                else:
                    ans+=(lf*rf)
        elif(s[k]=='^'):
                if(istrue==True):
                    ans+=lt*rf+rt*lf
                else:
                    ans+=lt*rt+lf*rf

        dict[temp] = ans
    print(dict)
    return dict[temp]



s="T|T&F^T"
i=0
j=len(s)-1
print(solve(s,i,j,True))
