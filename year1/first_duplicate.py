#Runtime: O(n) | Space:O(n)
#		  where n is the length of the array
def first_duplicate(array):
    #We can traverse through the list and at each val in array, map that value to the index of the array
	#We then change that index's val by negating it
		#Therefore, if we ever reach a number that links to an index's value that is negative, we know we already
		#encountered it.
    for i in range(len(array)):
        mappedIndex = abs(array[i]) - 1

        if array[mappedIndex] < 0:
            return abs(array[i])
        else:
            array[mappedIndex] *= -1
    return -1

#Runtime: O(n) | Space:O(n)
#		  where n is the length of the array
def first_duplicate2(array):
    #Initialize a dictionary to store values that have already been see
    #Traverse though the array
        #At each element, check to see if it's already in the seen Dictionary
            #If yes, then return that element
            #If no, add that element to the dictionary and move on to the next element
    #If we make it through the array with returning, simply return -1
    alreadySeen = {}
    for val in array:
        if val in alreadySeen:
            return val
        else:
            alreadySeen[val] = True
    return -1

array1 = [1, 2]
print(first_duplicate(array1))
#-1

array2 = [3, 1, 3, 1, 1, 4, 4]
print(first_duplicate(array2))
#3

array3 = [6, 6, 5, 1, 1, 1, 2, 2]
print(first_duplicate(array3))
#6

array4 = [6, 1, 8, 2, 2, 1, 7, 1, 8, 6]
print(first_duplicate(array4))
#2