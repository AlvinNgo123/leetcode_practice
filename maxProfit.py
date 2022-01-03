from typing import List

#Runtime: O(n) | Space: O(1)
def maxProfit(prices: List[int]) -> int:
	currMaxProfit = 0
	currMin = prices[0]

	for i in range(1, len(prices)):
		currMin = min(prices[i], currMin)
		currProfit = prices[i] - currMin
		currMaxProfit = max(currProfit, currMaxProfit)

	return currMaxProfit

#Runtime: O(n) | Space: O(n)
def maxProfitDP(prices: List[int]) -> int:
	profitArr = [0] * len(prices)
	currMin = prices[0]

	for i in range(1, len(prices)):
		if prices[i] < currMin:
			currMin = prices[i]

		currProfit = prices[i] - currMin
		if currProfit > profitArr[i-1]:
			profitArr[i] = currProfit
		else:
			profitArr[i] =  profitArr[i-1]


	return profitArr[-1]

#Runtime: O(n^2) | Space: O(1)
def maxProfitBruteForce(prices: List[int]) -> int:
	maxP = 0
	for i in range(len(prices)-1):
		for j in range(i+1, len(prices)):
			currP = prices[j] - prices[i]
			if (currP > 0) and (currP > maxP):
				maxP = currP

	return maxP


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
#5 because buy at 1 and sell at 6

prices = [7,6,4,3,1]
print(maxProfit(prices))
#0 because always at a loss so profit is 0

prices = [7,3,5,5,6,1]
print(maxProfit(prices))
#3 because buy at 3 and sell at 6
