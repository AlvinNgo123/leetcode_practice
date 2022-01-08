def isAnagramSort(s, t):
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

#Runtime: O(n) | Space: O(n)
def isAnagramDict(s, t):
    if len(s) != len(t):
        return False

    inS = {}
    for i in range(len(s)):
        if s[i] in inS:
            inS[s[i]] += 1
        else:
            inS[s[i]] = 1

    for i in range(len(t)):
        if (t[i] in inS) and (inS[t[i]] > 0):
            inS[t[i]] -= 1
        else:
            return False
    
    for key, value in inS.items():
        if value > 0:
            return False
    
    return True 

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
#True

s = "rat"
t = "car"
print(isAnagram(s, t))
#False