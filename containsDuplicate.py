from typing import List

#Runtime: O(n) | Space: O(n)
def containsDuplicate(nums: List[int]) -> bool:
	alreadySeen = {}

	for i in range(len(nums)):
		if nums[i] in alreadySeen:
			return True
		else:
			alreadySeen[nums[i]] = 1
	return False

#Runtime: O(nlogn) | Space: O(1)
def containsDuplicate2Pointers(nums: List[int]) -> bool:
	nums.sort()

	ptr1 = 0
	ptr2 = 1

	while ptr2 < len(nums):
		if nums[ptr1] == nums[ptr2]:
			return True
		ptr1 += 1
		ptr2 += 1
	return False

#Runtime: O(n^2) | Space: O(1)
def containsDuplicateBruteForce(nums: List[int]) -> bool:
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			if nums[i] == nums[j]:
				return True
	return False


nums = [1,2,3,1]
print(containsDuplicate(nums))
#true because there are two 1's

nums = [1,2,3,4]
print(containsDuplicate(nums))
#false 

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
#true 

