num1 = 11
num2 = 12

if num1<num2:
    min = num1
else:
    min = num2

for i in range(1,min+1):
    if (num1%i ==0) and (num2%i==0):
        hcf = i

print(hcf)