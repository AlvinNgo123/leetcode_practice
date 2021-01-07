#Runtime: O() | Space: O()
#		  where n is the length of "arr" array
def monotonic_array(arr):
	pass

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