#Runtime: O(n) | Space: O(1)
#         where n is the number of vals in array "arr"
def three_largest_num(arr):
	#Have three variables that keep track of the three largest numbers (low, med, high)
	#Iterate through arr and at each value, compare it to the three largest nums
		#Start comparison at high and go all the way to low
		#If the curr val is greater than a current "largest" num, shift the values starting from that pt down and add the new num
	#At the end, return the [low, med, high]

	high = None
	med = None
	low = None
	for val in arr:
		if high is None or val > high:
			low = med
			med = high
			high = val
		elif med is None or val > med:
			low = med
			med = val
		elif low is None or val > low:
			low = val
	return [low, med, high]


arr1 = [101, 23, 32, 11, 2, 3, 4, 400]
print(three_largest_num(arr1))
#[32, 101, 400]

arr2 = [14, 1, 17, -27, 8, 7]
print(three_largest_num(arr2))
#[8, 14, 17]
