import sys

max_val = sys.maxsize
def coin(coins,amount):
    n = len(coins)
    tab = [[ 0 for i in range(amount+1)] for j in range(n+1)]

    for i in range(amount+1):
        tab[0][i] = max_val-1

    for j in range(1,n+1):
        tab[j][0] = 0
    
    for i in range(1,amount+1):
        if (i%coins[0] == 0):
            tab[1][i] = i//coins[0]
        else:
             tab[1][i] = max_val-1   
        print(tab[1][i])      
        
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if  coins[i-1] <= j:
                tab[i][j] = min(tab[i][j-coins[i-1]]+1,tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
    
 
    if (tab[n][amount] == max_val-1):
        return -1
    else:
        return tab[n][amount]

coins = [1,2] 
amount = 1
n = coin(coins,amount)
print(n)