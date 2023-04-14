n = 123456

def rever(start,end,list1):
    while (start<end):
        list1[start],list1[end] = list1[end],list1[start]
        start =start+1
        end = end -1
    return list1

k =2
res = list(map(int, str(n)))
print(res)
length = len(res)-1
list1 = rever(0,length,res)
rever(0,k-1,list1)
rever(k,length,list1)
print(list1)
result="".join(map(str,list1))
# for i in list1:
#     result = result+str(i)
print(result)