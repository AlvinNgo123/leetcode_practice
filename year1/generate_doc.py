#Runtime: O(n+m) | Space: O(n)
#         where n is len of characters and d is len of document
def generate_doc(characters, document):
	#First check if the list of chars is less than document. If it is, we know its false
	#Traverse through list chars and add each char & their count to a dictionary
	#Now, traverse through the list document and compare each doc's char to the dict
		#If the doc's current char is in the dict, decrement that char's count
		#If the doc's current char isn't in the dict or that char's count is 0, return False
	#If you're able to traverse all the way to the end, we know we can return true.
	
	if len(characters) < len(document):
		return False
	
	charCountDict = {}
	for char in characters:
		if char in charCountDict:
			charCountDict[char] += 1
		else:
			charCountDict[char] = 1
	
	for char in document:
		if char in charCountDict:
			if charCountDict[char] == 0:
				return False
			charCountDict[char] -= 1
		else:
			return False
	return True

char1 = "&*&you^a%^&8766 _=-09     docanCMakemthisdocument"
doc1 = "Can you make this document &"
print(generate_doc(char1, doc1))

char2 = "estssa"
doc2 = "testing"
print(generate_doc(char2, doc2))