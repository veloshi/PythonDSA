# 1 to n
# def Print(n):
#     if n == 1:
#         print(n)
#         return 
#     Print(n-1)
#     print(n)

# Print(5)
# n to 1
def Print(n):
    if n == 0:
        return 1
    print(n)
    return Print(n-1)


Print(5)


