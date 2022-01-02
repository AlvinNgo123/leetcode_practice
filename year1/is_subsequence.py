#Runtime: O(n) | Space: O(1)
#         where n is the number of chars in string "t"
def is_subsequence(s, t):
	#First case: If both s and t are the same string, then s is a substring of t
	#Have two pointers. One to traverse s and the second to traverse t
	#Traverse through t one char at a time.
		#At each char, we want to check if the char matches the current char at s
		#If no, we only move the t ptr to the next char
		#If yes, we move both ptrs to their next char and then check to see if we already finished going through s
			#If we reached end of s, we know that s is a substring of t
	#If it reaches the end of t and we still haven't returned true, that means s is NOT a substring and we return False.

	if s == t:
		return True

	ptrS = 0
	for ptrT in range(len(t)):
		if s[ptrS] != t[ptrT]:
			ptrT += 1
		else:
			ptrT += 1
			ptrS += 1
			if ptrS == len(s):
				return True
	return False



s1 = "abc"
t1 = "ahbgdc"
print(is_subsequence(s1, t1))
#True

s2 = "axc"
t2 = "ahbgdc"
print(is_subsequence(s2, t2))
#False

s3 = "16-110"
t3 = "5122256-1810"
print(is_subsequence(s3, t3))
#True

s4 = ""
t4 = ""
print(is_subsequence(s4, t4))
#True