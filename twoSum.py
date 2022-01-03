from typing import List

#Runtime: O(nlogn) | Space: O(1)
def twoSum(nums: List[int], target: int) -> List[int]:
	for i in range(len(nums)):
		nums[i] = (nums[i], i)

	#Sort the list first in increasing order
	#Use two ptrs one for each end 
	nums.sort()
	ptr1 = 0
	ptr2 = len(nums)-1

	while ptr1 < ptr2:
		val1, idx1 = nums[ptr1]
		val2, idx2 = nums[ptr2]
		if target == (val1 + val2):
			return [idx1, idx2]
		elif target < (val1 + val2):
			ptr2 -= 1
		else:
			ptr1 += 1

	return [-1, -1]

	

#Runtime: O(n) | Space: O(n)
def twoSumDictionary(nums: List[int], target: int) -> List[int]:
	alreadySeen = {} #Key: element, Value: index 

	for i in range(len(nums)):
		difference = target - nums[i]
		if difference in alreadySeen:
			return [alreadySeen[difference], i]
		else:
			alreadySeen[nums[i]] = i
	return [-1, -1]

#Runtime: O(n^2) | Space: O(1)
def twoSumBruteForce(nums: List[int], target: int) -> List[int]:
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			#print("current sum - " + str(nums[i] + nums[j]))
			if (nums[i] + nums[j]) == target:
				return [i, j]

	return [-1, -1]



nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
#[0, 1]

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
#[1, 2]

nums = [3,3]
target = 6
print(twoSum(nums, target))
#[0, 1]