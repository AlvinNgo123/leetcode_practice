#Runtime: O(n) | Space: O(1)
#         where n is the length of the string
def valid_palindrome(s):
	#Empty string is palindrome
	if len(s) == 0:
		return True

	#Have two pointer: one at the beginning at list & one at the end 
	leftPtr = 0
	rightPtr = len(s) - 1

	#While the left pointer is less than the right pointer and the two chars at each ptr are the same:
	#Keep incrementing the left and decrementing the right
	#If chars differ, immediately return false
	isPalindrome = True
	while leftPtr < rightPtr:
		if s[leftPtr] == s[rightPtr]:
			leftPtr += 1
			rightPtr -= 1
		else:
			return False
	return isPalindrome


print(valid_palindrome('moom'))
# True
print(valid_palindrome('abcdcba'))
# True
print(valid_palindrome('raceacar'))
# False