def isSubsetSum(set, n, sum):
      
    # The value of subset[i][j] will be 
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset =([[False for i in range(sum + 1)] 
            for i in range(n + 1)])
      
    # If sum is 0, then answer is true 
    for i in range(n + 1):
        subset[i][0] = True
          
    # If sum is not 0 and set is empty, 
    # then answer is false 
    for i in range(1, sum + 1):
         subset[0][i]= False
              
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or 
                                subset[i - 1][j-set[i-1]])
    list1 = []
    for j in range((sum+1)//2):
        print(j)
        print(subset[3][j])
        if subset[3][j] == True:
            list1.append(j)
    print(list1)     
    mn = 100000
    for i in range(len(list1)):
        mn = min(mn,sum-(2*list1[i]))
            
    # print(mn) 
    # # uncomment this code to print table 
    # # for i in range(n + 1):
    # # for j in range(sum + 1):
    # # print (subset[i][j], end =" ")
    # # print()
    # return subset[n][sum]
    return mn
# Driver code
if __name__=='__main__':
    set = [5,5,11]
    sum1 = 0
    n = len(set)
    for i in range(len(set)):
        sum1 = sum1+set[i]
    print(isSubsetSum(set, n, sum1))
    # for i in range(len(set)):
    #     sum = sum+set[i]
    # if sum%2 != 0:
    #     print(False)
    # else :
    #      print(isSubsetSum(set, n, sum//2))
        