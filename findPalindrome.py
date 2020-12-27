def find_palindrome(s):
	#go through string and keep track of letter's and their count using a hashtable (dictionary)]
	#There can be no more than 1 letter that has an odd number of occurrences
	ht = {}
	for i in s:
		if i in ht:
			ht[i] = ht[i] + 1
		else:
			ht[i] = 1

	possibleP = 'a' * len(s)
	countOdd = 0
	currStart = 0
	currEnd = len(s)
	for key, val in ht.items():
		if ((val % 2) == 0):
			shift = val / 2
			while shift > 0:
				possibleP[currStart] = key
				currStart += 1
				possibleP[currEnd] = key 
				currEnd -= 1
		else:
			if ((len(s) % 2) != 0):
				return None
			elif countOdd > 0:
				return None
			else:
				tempVal = val
				while tempVal > 1:
					possibleP[currStart] = key
					currStart += 1
					possibleP[currEnd] = key 
					currEnd -= 1
					tempVal = tempVal - 2
				possibleP[(len(s)/2)] = key
	return possibleP

print(find_palindrome('momom'))
# momom