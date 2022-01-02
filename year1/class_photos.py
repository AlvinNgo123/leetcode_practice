#Runtime: O(nlogn) | Space: O(1)
#		  where n is length of one of the height lists
def classPhotos(redShirtHeights, blueShirtHeights):
    #Sort both the red shirt heights list and blue shirt heights list
	#Iniatilize the bool variable (redTaller) based on whether the first red height is larger or shorter than blue's first height
	#Iterate through both lists at the same time
		#At each spot, check the bool var (redTaller) to see which color shirt is supposed to taller
		#Check to see if current spots in list follow this pattern
			#If no, return False
	#If we reach the end of both lists successfully, we return True
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	redTaller = None
	if redShirtHeights[0] > blueShirtHeights[0]:
		redTaller = True
	elif redShirtHeights[0] < blueShirtHeights[0]:
		redTaller = False
	else:
		return False
	
	for i in range(len(redShirtHeights)):
		if redTaller == True:
			if redShirtHeights[i] < blueShirtHeights[i]:
				return False
		else:
			if redShirtHeights[i] > blueShirtHeights[i]:
				return False
			
    return True
