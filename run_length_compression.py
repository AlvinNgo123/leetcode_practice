#Runtime: O(n) | Space: O(n)
#         where n is the length of the string
def run_length_compression(string):
	#Initialize return array (later convert to string)
    #Have a curr counter that increments with every same character (initialized to 1)
	#Have a curr char that tracks the current character we're encoding (initialized to first char)
	#Go through string in one pass
	   #First check if letter in str is the currChar
		   #If no, we add the currCounter and currChar to the return array
				#Then we update the currChar to the letter and reset the currCounter to 1
		   #If yes, we check to see if currCounter is 9
		         # If yes, we add the currCounter and currChar to return array
					#Then, we reinitialize currCounter to 1
			     # If no, we simply increment the currCounter by 1
	#After finishing going through string, we have to push the last encoding run to return array
	#Convert return array to string and return it.
	
	returnArray = []
	returnStr = ""
	currCounter = 1
	currChar = string[0]
	
	for i in range(1, len(string)):
		letter = string[i]
		
		if letter != currChar:
			returnArray.append(str(currCounter))
			returnArray.append(currChar)
			currCounter = 1
			currChar = letter
		else:
			if currCounter == 9:
				returnArray.append(str(currCounter))
				returnArray.append(currChar)
				currCounter = 1
			else:
				currCounter += 1
	
	returnArray.append(str(currCounter))
	returnArray.append(currChar)
	return returnStr.join(returnArray)
	

string1 = "AAAAAAAAAAPPPLNNNN"
print(run_length_compression(string1))
#"9A1A3P1L4N"

string2 = "v"
print(run_length_compression(string2))
#"1v"

string3 = "bbaaaaaaB11"
print(run_length_compression(string3))
#"2b6a1B21"



