#Average/Worse Runtime: O(n^2) | Space:O(1)
#		  where n is the length of the array
#Best Case Runtime: O(n)
def bubble_sort(array):
    #Intialize a variable that keeps track of if a switch occurs during each pass to True
    #Continue doing passes until variable remains True at end of pass
        #reset swap var to False
        #Comptre each curr element with its next and swap if curr is greater than next
            #If swap occurs, change swap tracking variable to True
        #If not, iterate to next element
    #Return the array which is now sorted
    swapOccurred = True
    while swapOccurred == True:
        swapOccurred = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                swapOccurred = True
    return array
        
array1 = [3, 1, 2]
print(bubble_sort(array1))
#[1, 2, 3]

array2 = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print(bubble_sort(array2))
#[-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]

array3 = [31, 21, 12, -1, -2]
print(bubble_sort(array3))
#[-2, -1, 12, 21, 31]