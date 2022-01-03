from typing import List

#Runtime: O(n) | Space: O(1)
def maxProduct(nums: List[int]) -> int:
    overallMax = nums[0]
    priorMax = nums[0]
    priorMin = nums[0]

    for i in range(1, len(nums)):
        currMax = max(priorMax * nums[i], priorMin * nums[i], nums[i])
        currMin = min(priorMax * nums[i], priorMin * nums[i], nums[i])
        priorMax = currMax
        priorMin = currMin
        overallMax = max(currMax, overallMax)
    return overallMax
        

#Runtime: O(n) | Space: O(n)
def maxProductDP(nums: List[int]) -> int:
    productArr = [(0, 0)] * len(nums)

    productArr[0] = (nums[0], nums[0])
    for i in range(1, len(nums)):
        priorMax, priorMin = productArr[i-1]
        productArr[i] =  ( max(priorMax * nums[i], priorMin * nums[i], nums[i]), min(priorMax * nums[i], priorMin * nums[i], nums[i]) )

    maxP = productArr[0][0]
    for i in range(1, len(productArr)):
        maxP = max(maxP, productArr[i][0])  

    return maxP


nums = [2,3,-2,4]
print(maxProduct(nums))
#6 because [2, 3]

nums = [-2,0,-1]
print(maxProduct(nums))
#0