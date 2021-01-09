#Runtime: O() | Space: O()
#		  where n is the length of "arr" array
def max_subset_sum_non_adjacent(arr):
	pass

arr1 = [75, 105, 120, 75, 90, 135]
print(max_subset_sum_non_adjacent(arr1))
#330 because of [75, 120, 135] 

arr2 = [1, 2]
print(max_subset_sum_non_adjacent(arr2))
#2 because of [2]

arr3 = [3, 3, 3, 4, 10, 4]
print(max_subset_sum_non_adjacent(arr3))
#16 because of [3, 3, 10]