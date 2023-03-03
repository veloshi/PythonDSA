
# Below is the implementation of the above approach
def printSubsequence(input, output,set1):
	set1.add(output)
	# Base Case
	# if the input is empty print the output string
	if len(input) == 0:
		
		return                                                 
	# output is passed with including the
	# 1st character of input string
	printSubsequence(input[1:], output+input[0],set1)

	# output is passed without including the
	# 1st character of input string
	printSubsequence(input[1:], output,set1)
	return list(set1)

# Driver code
# output is set to null before passing in
# as a parameter
output = ""
set1 = set()
input = "12"

print(printSubsequence(input, output,set1))

#remove set and insert print(output) in base condition