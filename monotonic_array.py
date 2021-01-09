#Runtime: O(n) | Space: O(1)
#		  where n is the length of "arr" array
def monotonic_array(arr):
	#Handle base cases of empty and 1 element arrays being true
	#Have a current trend var that tracks the moment that we realize if the list is currently increasing or decreasing
	#Initialize the currTrend 
	#Iterate through the array and keep going until currTrend is filled
	#If currTrend isn't filled at the end of list, return True
	#Otherwise, now go through rest of list and see if it still fits the currTrend or deviates

	if len(arr) == 0 or len(arr) == 1:
		return True

	currTrend = None

	currIdx = 1  
	while currIdx < len(arr) and currTrend is None:
		 if arr[currIdx] == arr[currIdx-1]:
		 	currIdx += 1
		 elif arr[currIdx] > arr[currIdx-1]:
		 	currTrend = 'increasing'
		 	break
		 else:
		 	currTrend = 'decreasing'
		 	break

	if currTrend is None:
		return True

	while currIdx < len(arr):
		if arr[currIdx] > arr[currIdx-1] and currTrend == 'decreasing':
			return False
		elif arr[currIdx] < arr[currIdx-1] and currTrend == 'increasing':
			return False
		currIdx += 1

	return True

arr1 = [1, 2, 2, 3]
print(monotonic_array(arr1))
#True

arr2 = [6, 5, 4, 4]
print(monotonic_array(arr2))
#True

arr3 = [1, 2, 4, 5]
print(monotonic_array(arr3))
#True

arr4 = [1, 1, 1]
print(monotonic_array(arr4))
#True

arr5 = [-1, -5, -10, -1222]
print(monotonic_array(arr5))
#True

arr6 = [1, 3, 2]
print(monotonic_array(arr6))
#False