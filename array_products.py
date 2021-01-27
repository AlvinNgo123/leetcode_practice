#Runtime: O(n) | Space: O(n)
#		  where n is length of array
def array_products(array):
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
