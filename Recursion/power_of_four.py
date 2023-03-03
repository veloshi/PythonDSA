def isPowerOfFour(n):
    if n <=0:
        return False
    if n == 1 or n == 4 :
        return True
    if n%4 != 0 and n!=1:
        return False
    return isPowerOfFour(n//4)

if (isPowerOfFour(26//4)):
    print("Success")
else:
    print("failure")