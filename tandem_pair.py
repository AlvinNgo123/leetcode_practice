#Runtime: O(nlogn) | Space: O(1)
#		  where n is the number of pairs (length of 1 list)
def tandem_pair(bikers1, bikers2, maximize):
	#If maximize is true:
		#Sort one list in ascending order and the other in descending order
		#This will make sure one's maxes are matched with the other's mins, maximimzing the maxs chance of winning
	#If maximize is false:
		#Sort both lists in ascending order
		#This will put both max values against each other, minimizing final tandem val
	#Traverse thorugh both lists at once
		#At each index, add the higher value to the final tandem value
	if maximize == True:
		bikers1.sort(reverse=True)
	else:
		bikers1.sort()
	bikers2.sort()
	
	tandem = 0
	for i in range(len(bikers1)):
		tandem += max(bikers1[i], bikers2[i])
	
	return tandem

bikerL1 = [1, 2, 1, 9, 12, 3]
bikerL2 = [3, 3, 4, 6, 1, 2]
maximize = False
print(tandem_pair(bikerL1, bikerL2, maximize))
#30

bikerL1 = [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1]
bikerL2 = [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32]
maximize = True
print(tandem_pair(bikerL1, bikerL2, maximize))
#816