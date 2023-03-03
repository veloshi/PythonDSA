def isPowerOfthree(n):
    if n <=0:
        return False
    if n == 1 or n == 4 :
        return True
    if n%3 != 0 and n!=1:
        return False
    return isPowerOfthree(n//3)

if (isPowerOfthree(27//3)):
    print("Success")
else:
    print("failure")