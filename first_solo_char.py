#Runtime: O(n) | Space: O(n)
#		  where n is the length of the string
def first_solo_char(string):
	#Initialize a dict that store the strings chars and its count
	#Iterate through string & fill up dict
		#dictionary will fill up as you go left to right with first pair in dict being first char of string
		#KEY: char
		#VALUE: [firstIndex, count]
			#On char's first occurence: update first index and initalize count to 1
			#After first occurence, only update count by incrementing value
	#Now, iterate thorugh dictionary (key, val)
		#If a val is equal to 1, return that key. Else, continue.
	seenDict = {}
	for i in range(len(string)):
		currChar = string[i]
		if currChar in seenDict:
			thisVal = seenDict[currChar]
			thisVal[1] += 1 
		else:
			seenDict[currChar] = [i, 1]
	
	for key, val in seenDict.items():
		if val[1] == 1:
			return val[0]
	
	#Should never reach here unless no solo char
	return -1

string1 = "hello hallo"
print(first_solo_char(string1))
#1

string2 = "12345"
print(first_solo_char(string2))
#0

string3 = "ababcabab"
print(first_solo_char(string3))
#4