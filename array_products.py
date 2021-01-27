#Runtime: O(n) | Space: O(n)
#		  where n is length of array
def array_products(array):
    #We can make three additional arrays
		#1) array with products of all values to the left of an index
		#2) array with products of all values to the right of an index
		#3) final array that multiplies the products of left and right of index
	#We need to have a currentLeftProduct and currentRightProduct to keep track of our running product
	#We first fill up the left (start from beginning), then we fill the right (start from end) 
		#Each time, we use the current(Left or Right)Product to fill out curernt index of array 
		#Then, we update the current(Left or Right)Product to include the current value
	#Finally, go through final list and multiply the corersponding index's val in left and right to get final value
    leftProducts = [0 for x in range(len(array))]
    rightProducts = [0 for y in range(len(array))]
    finalProducts = [0 for z in range(len(array))]
    currLeftProd, currRightProd = 1, 1

    for i in range(len(array)):
        leftProducts[i] = currLeftProd
        currLeftProd *= array[i]
    for j in range(len(array)-1, -1, -1):
        rightProducts[j] = currRightProd
        currRightProd *= array[j]
    for k in range(len(finalProducts)):
        finalProducts[k] = leftProducts[k] * rightProducts[k]
    return finalProducts

#Runtime: O(n) | Space: O(n)
#		  where n is length of array
def array_products2(array):
    #This is a just a cleaner version of the other optimal soln
	#However, we no longer need to have the left and right products array
	#We can just modify the return array with our left products first
	#Then, we loop backwards and then multiply the current running right prod with the return 
	#Then, just return final product
    finalProducts = [0 for z in range(len(array))]
    currLeftProd = 1
    currRightProd = 1

    for i in range(len(array)):
        finalProducts[i] = currLeftProd
        currLeftProd *= array[i]

    for j in range(len(array)-1, -1, -1):
        finalProducts[j] *= currRightProd
        currRightProd *= array[j]
    
    return finalProducts

#Runtime: O(n^2) | Space: O(n)
#		  where n is length of array
def array_products3(array):
    #Brute force method
	#Iterate through each element in the array
	#At each iteration, multiply everything but skip the curr element
	#then, place the prod into the return list at the curr element's index
    productArr = []
    for i in range(len(array)):
        startIdx = 0
        currProd = 1
        while startIdx < len(array):
            if startIdx != i:
                currProd *= array[startIdx]
            startIdx += 1
        productArr.append(currProd)
    return productArr

array1 = [-1, -1, -1, -1] 
print(array_products(array1))
#[-1, -1, -1, -1]

array2 = [9, 3, 2, 1, 9, 5, 3, 2]
print(array_products(array2))
#[1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290]

array3 = [1, 8, 6, 2, 4] 
print(array_products(array3))
#[384, 48, 64, 192, 96]
