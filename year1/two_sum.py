#Runtime: O(nlogn) | Space: O(1)
#         where n is the number of vals in list
def two_sum(nums, target):
	#First sort the list in ascending order
	#Have 1 ptr at the beginning of the list (smallest num) & 1 ptr at the end of the list (largest num)
	#While the left ptr is less than the right ptr, continue loop 
		#At each loop, first check to see if the two values sum to the target
		#If they do, return the two values
		#If they dont, check to see if the sum is less than or greater than the target
			#If greater, decrement the right ptr(move to left)
			#If less than, increment the left ptr(move to right)
	nums.sort()
	leftPtr = 0
	rightPtr = len(nums) - 1
	while leftPtr < rightPtr:
		currSum = nums[leftPtr] + nums[rightPtr]
		if currSum == target:
			return [nums[leftPtr], nums[rightPtr]]
		elif currSum > target:
			rightPtr -= 1
		else:
			leftPtr += 1
	return []


#Runtime: O(n) | Space: O(n)
#         where n is the number of vals in list 
def two_sum2(nums, target):
	#Go through each num in list and gets its difference from the target value
	#Check to see if the difference has been seen before by checking the "seen" dictionary
	#If it has, then return the [difference, current num]. Otherwise, add the current num to the dictionary
	seenDict = {}
	for num in nums:
		difference = target - num
		if difference in seenDict:
			return [difference, num]
		else:
			seenDict[num] = True
	return []


#Runtime: O(n^2) | Space: O(1)
#         where n is the number of vals in list
def two_sum3(nums, target):
	#Go through every possible pair of numbers to find the target
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			currSum = nums[i] + nums[j]	
			if currSum == target:
				return [nums[i], nums[j]]
	return []


nums1 = [2, 7, 11, 15] 
target1 = 9
print(two_sum(nums1, target1))
#[2, 7]

nums2 = [3, 2, 4] 
target2 = 6
print(two_sum(nums2, target2))
#[2, 4]

nums3 = [3, 3] 
target3 = 6
print(two_sum(nums3, target3))
#[3, 3]

nums4 = [3, 5, -4, 8, 11, 1, -1, 6] 
target4 = 10 
print(two_sum(nums4, target4))
#[-1, 11] 