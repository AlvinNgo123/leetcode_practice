#Average/Worse Runtime: O(n^2) | Space:O(1)
#		  where n is the length of the array
#Best Case Runtime: O(n^2)
def selection_sort(array):
    #Have a ptr that points to the first index of the unsorted list (this will be where swap occurs) i.e. swapPosition
    #Have another ptr that iterates through all the values starting from that first ptr to the end of list and gets the index of its minimum value i.e checkPosition
    #Perform the swap and then continue until the first ptr reaches the end of the list

    for swapPosition in range(0, len(array)):
        currMinVal = array[swapPosition]
        currMinIdx = swapPosition
        for checkPosition in range(swapPosition+1, len(array)):
            if currMinVal > array[checkPosition]:
                currMinVal = array[checkPosition]
                currMinIdx = checkPosition
        temp = array[swapPosition]
        array[swapPosition] = currMinVal
        array[currMinIdx] = temp
    return array
        

array1 = [3, 1, 2]
print(selection_sort(array1)) 
#[1, 2, 3]

array2 = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print(selection_sort(array2))
#[-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]

array3 = [31, 21, 12, -1, -2]
print(selection_sort(array3))
#[-2, -1, 12, 21, 31]