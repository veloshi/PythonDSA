arr= [3,5,2,2,4,1,1,8,1,1,9,8,8,8,8,7,7,7]
arr=arr[::-1]
length = 0

def frequency(arr,n):
    ind = 1
    count = 1
    element = arr[0]
    print(n)
    while ind<n:
        if arr[ind] == arr[ind-1]:
            count = count+1
            ind = ind+1
        else:
            print(element,count)
            element= arr[ind]
            count = 1
            ind = ind+1
    print(element,count)

n=len(arr)
frequency(arr,n)        
    
 