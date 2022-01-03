def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    
    maxLength = 0
    currMaxLength = 0
    alreadySeen = {}
    for i in range(len(s)):
        if s[i] not in alreadySeen:
            currMaxLength += 1
            alreadySeen[s[i]] = True
        else:
            if currMaxLength > maxLength:
                maxLength = currMaxLength
            currMaxLength = 1
            alreadySeen = {s[i]: True}
    
    if currMaxLength > maxLength:
        maxLength = currMaxLength
    return maxLength

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
#3 because "abc"

s = "bbbbb"
print(lengthOfLongestSubstring(s))
#1

s = "pwwkew"
print(lengthOfLongestSubstring(s))
#3 because "wke"