#Runtime: O(n) | Space: O(1)
#		  where n is the length of "arr" array
def max_subset_sum_non_adjacent(arr):
	#From looking at the 2nd soln (below this one), we can see that we only need to keep track of two values
	#The max at that specific index is either the sum of that current value plus the maxSum at the index two spots before or the maxSum at the previous index
	#Due to this, we just need to keep track of and update the prevMaxSum and prevPrevMaxSum.
	#Everything else remains the same so look at the 2nd soln for more details
	if len(arr) == 0:
		return 0

	prevPrevMaxSum = arr[0]
	if len(arr) == 1:
		return prevPrevMaxSum

	prevMaxSum = arr[1]
	if len(arr) == 2:
		return prevMaxSum

	for i in range(2, len(arr)):
		currMaxSum = max(prevMaxSum, arr[i]+prevPrevMaxSum)
		prevPrevMaxSum = prevMaxSum
		prevMaxSum = currMaxSum

	return prevMaxSum


#Runtime: O(n) | Space: O(n)
#		  where n is the length of "arr" array
def max_subset_sum_non_adjacent2(arr):
	#Check if empty list and return 0
	#First initialize a list (maxArr) of same length as arr and initialize them all to 0.
	#Fill the first index of maxArr with first value of arr.
		#Then, check if length of arr is 1 and if it is, return that first index's value
	#Fill the second index of maxArr with max(arr[0], arr[1])
		#Then, check if length of arr is 2 and if it is, return the second index's value 
	#This maxArr would indicate at each index, what the max subset sum would be if the list ended at that index
		#We go through remaining vals in arr and fill its corresponding maxArr value by using the following formula   
		#maxArr[i] = max(arr[i]+maxArr[i-2], maxArr[i-1])
	#Return the last index's value

	if len(arr) == 0:
		return 0

	maxArr = [0 for x in range(len(arr))]

	maxArr[0] = arr[0]
	if len(arr) == 1:
		return maxArr[0]

	maxArr[1] = max(arr[0], arr[1])
	if len(arr) == 2:
		return maxArr[1]

	for i in range(2, len(maxArr)):
		maxArr[i] = max(arr[i] + maxArr[i-2], maxArr[i-1])

	return maxArr[-1]




arr1 = [75, 105, 120, 75, 90, 135]
print(max_subset_sum_non_adjacent(arr1))
#330 because of [75, 120, 135] 

arr2 = [1, 2]
print(max_subset_sum_non_adjacent(arr2))
#2 because of [2] 

arr3 = [3, 3, 3, 4, 10, 4]
print(max_subset_sum_non_adjacent(arr3))
#16 because of [3, 3, 10]