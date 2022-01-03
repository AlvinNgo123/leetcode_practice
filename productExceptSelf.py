from typing import List

#Runtime: O(n) | Space: O(n)
def productExceptSelf(nums: List[int]) -> List[int]:
	productArr = [1] * len(nums)

	multiple = 1
	for i in range(len(nums)):
		productArr[i] = multiple
		multiple *= nums[i]
		#print(productArr)

	multiple = 1
	for j in range(len(nums)-1, -1, -1):
		productArr[j] *= multiple
		multiple *= nums[j]

	return productArr


#Runtime: O(n^2) | Space: O(1)
def productExceptSelfBruteForce(nums: List[int]) -> List[int]:
	productArr = [0] * len(nums)

	for i in range(len(nums)):
		currIdx = 0
		currProduct = 1
		while currIdx < len(nums):
			if currIdx != i:
				currProduct *= nums[currIdx]
			currIdx += 1
		productArr[i] = currProduct
	return productArr


nums = [1,2,3,4]
print(productExceptSelf(nums))
# [24,12,8,6]

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
# [0,0,9,0,0]