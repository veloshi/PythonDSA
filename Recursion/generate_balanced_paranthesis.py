# Python program to print all the combinations of balanced parenthesis.

# function which generates all possible n pairs of balanced parentheses.
# open : count of the number of open parentheses used in generating the current string s.
# close : count of the number of closed parentheses used in generating the current string s.
# s : currently generated string/
# ans : a vector of strings to store all the valid parentheses.


# def generateParenthesis(n, Open, close, s, ans):

# 	# if the count of both open and close parentheses reaches n, it means we have generated a valid parentheses.
# 	# So, we add the currently generated string s to the final ans and return.
# 	if(Open == n and close == n):
# 		ans.append(s)
# 		return

# 	# At any index i in the generation of the string s, we can put an open parentheses only if its count until that time is less than n.
# 	if(Open < n):
# 		generateParenthesis(n, Open+1, close, s+"{", ans)

# # At any index i in the generation of the string s, we can put a closed parentheses only if its count until that time is less than the count of open parentheses.
# 	if(close < Open):
# 		generateParenthesis(n, Open, close + 1, s+"}", ans)


# n = 3

# # ans is created to store all the possible valid combinations of the parentheses.
# ans = []

# # initially we are passing the counts of open and close as 0, and the string s as an empty string.
# generateParenthesis(n, 0, 0, "", ans)

# # Now, here we print out all the combinations.
# for s in ans:
# 	print(s)





































































































































































    

    #return v

open = 3
close = 3
v = []
# op = ""

solve(open,close,"",v)
for k in v:
    print(k)
