# # Python3 program to check if a
# # given string is a scrambled
# # form of another string
#         # string s= s1+" "+s2;
#         # if(s1==s2) return m[s]= true;
#         # if(s1.size()<=1 or s2.size()<=1) return false;
#         # if(m.find(s)!=m.end()) return m[s];
# def isScramble(S1: str, S2: str):

# 	# Strings of non-equal length
# 	# cant' be scramble strings
# 	if len(S1) != len(S2):
# 		return False

# 	n = len(S1)

# 	# Empty strings are scramble strings
# 	if not n:
# 		return True

# 	# Equal strings are scramble strings
# 	if S1 == S2:
# 		return True

# 	# Check for the condition of anagram
# 	if sorted(S1) != sorted(S2):
# 		return False

	
# 	for i in range(1, n):
		
# 		# Check if S2[0...i] is a scrambled
# 		# string of S1[0...i] and if S2[i+1...n]
# 		# is a scrambled string of S1[i+1...n]
# 		if (isScramble(S1[:i], S2[:i]) and
# 			isScramble(S1[i:], S2[i:])):
# 			return True

# 		# Check if S2[0...i] is a scrambled
# 		# string of S1[n-i...n] and S2[i+1...n]
# 		# is a scramble string of S1[0...n-i-1]
# 		if (isScramble(S1[n-i:], S2[:i]) and
# 			isScramble(S1[:n-i], S2[i:])):
# 			return True

# 	# If none of the above
# 	# conditions are satisfied
# 	return False

# # Driver Code
# if __name__ == "__main__":
	
# 	S1 = "coder"
# 	S2 = "ocred"
	
# 	if (isScramble(S1, S2)):
# 		print("Yes")
# 	else:
# 		print("No")

# # This code is contributed by sgshah2


#MEMOIZED Version :
# Declaring unordered map globally
map={}
# Python3 program to check if a
# given string is a scrambled
# form of another string
def isScramble(S1: str, S2: str):
     
    # Strings of non-equal length
    # cant' be scramble strings
    if len(S1) != len(S2):
        return False
 
    n = len(S1)
 
    # Empty strings are scramble strings
    if not n:
        return True
 
    # Equal strings are scramble strings
    if S1 == S2:
        return True
 
    # Check for the condition of anagram
    if sorted(S1) != sorted(S2):
        return False
     
    # Checking if both Substrings are in
    # map or are already calculated or not
    if(S1+' '+S2 in map):
        return map[S1+' '+S2]
     
    # Declaring a flag variable
    flag = False
 
    for i in range(1, n):
         
        # Check if S2[0...i] is a scrambled
        # string of S1[0...i] and if S2[i+1...n]
        # is a scrambled string of S1[i+1...n]
        if (isScramble(S1[:i], S2[:i]) and
            isScramble(S1[i:], S2[i:])):
            flag = True
            return True
 
        # Check if S2[0...i] is a scrambled
        # string of S1[n-i...n] and S2[i+1...n]
        # is a scramble string of S1[0...n-i-1]
        if (isScramble(S1[-i:], S2[:i]) and
            isScramble(S1[:-i], S2[i:])):
            flag = True
            return True
     
    # Storing calculated value to map
    map[S1+" "+S2] = flag
     
    # If none of the above
    # conditions are satisfied
    return False
 
# Driver Code
if __name__ == "__main__":
     
    S1 = "great"
    S2 = "rgate"
     
    if (isScramble(S1, S2)):
        print("Yes")
    else:
        print("No")