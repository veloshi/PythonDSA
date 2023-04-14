def armstrong(num):
    digit = 0
    while num>0:
        div = num%10
        digit = digit +div*div*div
        num =num//10
    return digit

num = 1532
if (armstrong(num) == num):
    print("Armstrong")
else:
    print("not an armstrong") 
# print(armstrong(num))