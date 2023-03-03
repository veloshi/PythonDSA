a = "11"
b = "11"
res = ""
carry = 0
#while performing calculation we start from right but in array we start from left hence we will reverse in order to perform the operations from right side
a,b = a[::-1],b[::-1]
for i in range(max(len(a),len(b))):
    digitA = ord(a[i]) - ord("0") if i<len(a) else 0
    digitB = ord(a[i]) - ord("0") if i<len(b) else 0

    total = digitA+digitB+carry
    char = str(total%2)
    res = char+res
    carry = total//2

if carry != 0:
    res = "1"+res
print(res)