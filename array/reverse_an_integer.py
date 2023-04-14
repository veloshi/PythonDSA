def reverse(num):
    rev = 0 
    while num>0:
        div = num%10
        rev = rev*10 + div
        num = num//10
    return rev


num = 12345
print(reverse(num))