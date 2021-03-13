#Runtime: O(n) | Space: O(n)
#		  where n is the length of the string.
def reverse_words_in_str(string):
	#Initialize a list (allWords) for all the words in the string
	#Initialize a currWord variable to empty string
	#Iterate through all the chars in the string
		#Each time we check if the current char is space ("")
			#If no, we append this char to the currWord list and move on 
			#If yes, we append currWord to the allWords list & reset currWord var to empty string
	#Traverse allWords list in reverse order in order to make a reversedList
	#Now, use the join function with a space as delimiter to join all words in reversedList and set to reversedStr
	#Return the reversedStr
	allWords = []
	currWord = []
	
	space = " "
	for index in range(len(string)):
		if string[index] == space or (index == (len(string)-1)):
			if index == (len(string)-1):
				currWord.append(string[index])
			finalWord = "".join(currWord)
			allWords.append(finalWord)
			currWord = []
		else:
			currWord.append(string[index])
	
	reversedWords = []
	for i in range(len(allWords)-1, -1, -1):
		reversedWords.append(allWords[i])
	
	reversedStr = " ".join(reversedWords)
			
	return reversedStr

str1 = "What is your name?"
print(reverse_words_in_str(str1))
#"name? your is What"