# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
# Driver code
n = 3
count = 0
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods                                                                                     
# count = 0
# def hanoi(disks, source, auxiliary, target):
#   global count
#   if disks == 1:
#     count = count + 1
#     return
 
#   hanoi(disks - 1, source, target, auxiliary)
#   count = count + 1
#   hanoi(disks - 1, auxiliary, source, target)
 
 
# disks = 3
# #int(input('Enter number of disks: '))
# hanoi(disks, 'A', 'B', 'C')
# print("Minimum number of disks move: ", count)