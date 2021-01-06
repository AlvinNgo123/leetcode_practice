#Method works but IS NOT allowed due to problem constraints
#Runtime: O(n) | Space: O(n)
#		  where n is the length of "nums" array
def move_zeroes(nums):
	#Create a new array of the same size as the nums and initialize all to 0
	#Then have a pointer that starts at the first index of this new array
	#Iterate through each val in original nums array
		#If the val is non-zero, change the corresponding index val in new array to this val
		#Then, iterate pointer to next index of new array
	#Return the new array

	finalArr = [0 for x in range(len(nums))]
	currPtr = 0

	for val in nums:
		if val != 0:
			finalArr[currPtr] = val
			currPtr += 1

	return finalArr


nums1 = [0, 1, 0, 0, 0, 3, 4, 0]
print(move_zeroes(nums1))
#[1, 3, 4, 2, 2, 2, 2, 2]

nums2 = [0, 1, 0, 3, 12]
print(move_zeroes(nums2))
#[1, 3, 12, 0, 0]