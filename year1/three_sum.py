def three_sum(nums): 
	#Loop through all possible triples
	#Check to see if current triple sums to 0
	#If it does, add the triple to resultant list

	resultList = []
	for i in range(len(nums)-2):
		for j in range(i+1, len(nums)-1):
			for k in range(j+1, len(nums)):
				currSum = nums[i] + nums[j] + nums[k]
				if currSum == 0:
					resultList.append([nums[i], nums[j], nums[k]])

	return resultList

nums1 = [12, 3, 1, 2, -6, 5, -8, 6]
print(three_sum(nums1))
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

nums2 = []
print(three_sum(nums2))
# []

nums3 = [0]
print(three_sum(nums3))
# []

nums4 = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums4))
# [[-1,-1, 2], [-1, 0, 1]]
