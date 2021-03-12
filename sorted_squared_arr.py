def sorted_squared_arr(array):	
	#Separate the negatives and positives
	negatives = []
	positives = []
	
	for val in array:
		if val < 0:
			negatives.append(val*val)
		else:
			positives.append(val*val) 
	
	print(negatives)
	print(positives)

	pointerNeg = len(negatives) - 1
	pointerPos = 0

	currentIdx = 0
	while currentIdx < len(array):
		if pointerPos == len(positives) and pointerNeg >= 0:
			array[currentIdx] = negatives[pointerNeg]
			pointerNeg -= 1
		elif pointerNeg < 0 and pointerPos < len(positives):
			array[currentIdx] = positives[pointerPos]
			pointerPos += 1
		elif negatives[pointerNeg] < positives[pointerPos]:
			array[currentIdx] = negatives[pointerNeg]
			pointerNeg -= 1
		elif negatives[pointerNeg] >= positives[pointerPos]:
			array[currentIdx] = positives[pointerPos]
			pointerPos += 1
		currentIdx += 1
			
	return array

array1 = [-7, -3, 1, 9, 22, 30]
print(sorted_squared_arr(array1))