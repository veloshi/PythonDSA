# from functools import reduce
# list1 =[1,2,3,4,5]

# # list2 = list(map(lambda x:x*3,list1))
# # print(list2)

# # list3 = list(filter(lambda x:x>3,list1))
# # print(list3)

# list2 = reduce(lambda a,b:a+b,list1)
# print(list2)
 
# n = 273**0.33
# print(n)

num1 = 4
num2 =6

if num1>num2:
    greater = num1
else:
    greater = num2
while(True):
    if (greater%num1 == 0 and greater %num2==0):
        lcm = greater
        break
    greater +=1

print(lcm)