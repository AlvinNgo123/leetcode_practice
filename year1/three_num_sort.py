#Runtime: O(n) | Space: O(1)
#		  where n is the length of array 
def three_num_sort(array, order):
    #Let's split array into sorted and unsroted section
		#In the beginning sorted is empty and unsorted is the entire array
		#Give a pointer indicating where the beginning of unsorted list is
			#This would be the swapPosition
	#Iterate through order
		#Iterate through array
			#If array element == order element
				#Perform swap and iterate swapPosition
	swapPosition = 0
	for i in range(3):
		for j in range(swapPosition, len(array)):
			if array[j] == order[i]:
				temp = array[j]
				array[j] = array[swapPosition]
				array[swapPosition] = temp
				swapPosition += 1
	return array
			
array1 = [0, 10, 10, 10, 10, 10, 25, 25, 25, 25, 25]
order1 = [25, 10, 0]
print(three_num_sort(array1, order1))
#[25, 25, 25, 25, 25, 10, 10, 10, 10, 10, 0]	
