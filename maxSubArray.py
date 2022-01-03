from typing import List

#Runtime: O(n) | Space: O(1)
def maxSubArray(nums: List[int]) -> int:
    #just keep track of the prior max instead of having another array
    maxSum = nums[0]
    priorMax = nums[0]

    for i in range(1, len(nums)):
        currMax = max(priorMax + nums[i], nums[i])
        priorMax = currMax
        maxSum = max(maxSum, currMax)
    return maxSum

#Runtime: O(n) | Space: O(n)
def maxSubArrayDP(nums: List[int]) -> int:
    maxArr = [0] * len(nums)

    maxArr[0] = nums[0]
    for i in range(1, len(maxArr)):
        maxArr[i] = max(maxArr[i-1] + nums[i], nums[i])
    
    #get the max of maxArr
    maxSum = maxArr[0]
    for i in range(1, len(maxArr)):
        maxSum = max(maxSum, maxArr[i])

    return maxSum
    
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
#6 because [4, -1, 2, 1]

nums = [1]
print(maxSubArray(nums))
#1

nums = [5,4,-1,7,8]
print(maxSubArray(nums))
#23

'''
Each element, you either add yourself to the prior count or you start over as the largest
At the end, go through the maxArr and find the maximum value
arr = [-2,1,-3,4,-1,2,1,-5,4]
maxArr = [-2, 1, -2, 4, 3, 5, 6, 1, 5]
maxArr[i] = max(maxArr[i-1] + arr[i], arr[i])
return max(maxArr)
'''