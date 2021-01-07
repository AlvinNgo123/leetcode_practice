#Runtime: O(n) | Space: O(1)
#		  where n is the length of "nums" array
def move_zeroes(nums):
	#Have two pointers. One for the swap position and the other to keep current track
	#Current ptr starts at the first element
	#Swap ptr starts at the first non-zero element starting from the right.

	#While the current ptr remains less than the swap ptr (to the left)
		#We check to see if current ptr's value is zero
			#If yes, we swap current ptr's val with swap ptr's val
			#Then, we shift swap ptr to the left until we reach another 0
	#At the end, return the nums array
	currPtr = 0
	swapPtr = len(nums)-1

	#get swapPtr to position of first non-zero element (if it exists)
	while (nums[swapPtr] == 0) and (swapPtr > currPtr):
		swapPtr -= 1 
	
	while currPtr < swapPtr:
		if nums[currPtr] == 0:
			tempVal = nums[currPtr]
			nums[currPtr] = nums[swapPtr]
			nums[swapPtr] = tempVal

			swapPtr -= 1
			while (nums[swapPtr] == 0) and (swapPtr > currPtr):
				swapPtr -= 1

		currPtr += 1

	return nums


#Method works but IS NOT allowed due to problem constraints
#Runtime: O(n) | Space: O(n)
#		  where n is the length of "nums" array
def move_zeroes2(nums):
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
#[1, 3, 4, 0, 0, 0, 0, 0]

nums2 = [0, 1, 0, 3, 12]
print(move_zeroes(nums2))
#[1, 3, 12, 0, 0]