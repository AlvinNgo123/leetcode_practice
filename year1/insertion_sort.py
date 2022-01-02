#Average/Worse Runtime: O(n^2) | Space:O(1)
#		  where n is the length of the array
#Best Case Runtime: O(n)
def insertion_sort(array):
    #Iterate through array and have the sorted list be on the left side of array and unsorted on the right side of array
    #Keep swapping the current value back until it reaches a position where it's larger than the one on its left.
    for i in range(1, len(array)):
        currVal = i
        while (array[currVal] < array[currVal-1]) and (currVal > 0):
            temp = array[currVal]
            array[currVal] = array[currVal-1]
            array[currVal-1] = temp
            currVal -= 1
    return array
        

array1 = [3, 1, 2]
print(insertion_sort(array1))
#[1, 2, 3]

array2 = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print(insertion_sort(array2))
#[-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]

array3 = [31, 21, 12, -1, -2]
print(insertion_sort(array3))
#[-2, -1, 12, 21, 31]