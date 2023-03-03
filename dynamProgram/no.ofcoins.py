#it will calculate the no. of ways a certain amount can be computed using given coins which can be repeated

def coin(coins,amount):
    n = len(coins)
    tab = [[ 0 for i in range(amount+1)] for j in range(n+1)]

    for i in range(amount+1):
        tab[0][i] = 0

    for j in range(1,n+1):
        tab[j][0] = 1
        
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if (coins[i-1] <= j):
                tab[i][j] = tab[i-1][j] + tab[i][j-coins[i-1]]
            else:
                tab[i][j] = tab[i-1][j]
                    
    return tab[n][amount]                                                                                           

coins = [3] 
amount = 1
n = coin(coins,amount)
print(n)