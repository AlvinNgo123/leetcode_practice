#Runtime: O(nlogn + mlogm) | Space: O(1)
#         where n is the length of arr1 and m is the length of arr2
def min_abs_difference(arr1, arr2):
	#First, sort both arrays in ascending order
	#Then, have two different ptrs and place both at the beginning of each array
	#Get the abs difference at the current pair
		#If the diff is 0, we found smallest so return the curr pair
		#Else, compare this diff to current min diff
			#If less than, update the diff
			#Regardless of less than or greater, increment the ptr that pointing to the smaller value
	#At the end, return the min pair

	arr1.sort()
	arr2.sort()

	currMinDiff = None
	currMinPair = []

	ptr1, ptr2 = 0, 0
	while ptr1 < len(arr1) and ptr2 < len(arr2):
		thisDiff = abs(arr1[ptr1] - arr2[ptr2])
		
		if thisDiff == 0:
			return [arr1[ptr1], arr2[ptr2]]

		if currMinDiff is None or currMinDiff > thisDiff:
			currMinDiff = thisDiff
			currMinPair = [arr1[ptr1], arr2[ptr2]]

		if arr1[ptr1] > arr2[ptr2]:
			ptr2 += 1
		else:
			ptr1 += 1 

	return currMinPair


#Runtime: O(nm) | Space: O(1)
#         where n is the length of arr1 and m is the length of arr2
def min_abs_difference2(arr1, arr2):
	#loop though all possible pair combination and calculate the abs difference.
	#keep track of the current minimum val (& corresponding pair) and update when a new min difference comes up.
	#return the final min pair

	currMinDiff = None
	currMinPair = []

	for i in range(len(arr1)):
		for j in range(len(arr2)):
			thisDiff = abs(arr1[i] - arr2[j])

			if currMinDiff is None or currMinDiff > thisDiff:
				currMinDiff = thisDiff
				currMinPair = [arr1[i], arr2[j]]

	return currMinPair



arr1_1 = [1, 6, 10, 15]
arr1_2 = [3]
print(min_abs_difference(arr1_1, arr1_2))
#[1, 3]

arr2_1 = [-1, 5, 10, 20, 28, 3]
arr2_2 = [26, 134, 135, 15, 17]
print(min_abs_difference(arr2_1, arr2_2))
#[28, 26]
