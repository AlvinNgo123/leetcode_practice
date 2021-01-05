#Runtime: O(nm) | Space: O(1)
#         where n is the length of arr1 and m is the length of arr2
def min_abs_difference(arr1, arr2):
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
