# s1 = "ABAc"
# s2 = ""
# for i in range(len(s1)-1,-1,-1):
#     s2=s2+s1[i]

# if s1 == s2:
#     print("Pallindrome")
# else:
#     print("Not a pallindrome")
def recur(num):
    if num<10:
        return num
    else:
        return int(str(num%10)+str(num//10))

def func1(num):
    if num == recur(num):
        return True
    return False

num = 121
if func1(num):
    print("Pallindrome")
else:
    print("Not a pallindrome")
