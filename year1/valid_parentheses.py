#Runtime: O(n) | Space:O(n)
#		  where n is the length of the array
def valid_parentheses(s):
    #Handle base case of empty string
    #Initialize a stack to keep track of all open brackets
    #Iterate through the string char by char
    #If char is an open bracket
        #Add that char to the open brackets stack
    #If char is a closing bracket
        #if stack is empty, return False
        #Else, Pop off the top open bracket from the open brackets stack
            #Compare the open bracket with the curr char
                #if they're the correct open and close pair, continue on
                #Else, return False
    #After full traversal, if stack is non empty return False. Else, return True
    if s == "":
        return True
    
    allOpens = {"(", "[", "{"}
    allCloses = {")", "]", "}"}
    openStack = []
    for bracket in s:
        if bracket in allOpens:
            openStack.append(bracket)
        elif bracket in allCloses:
            if len(openStack) == 0:
                return False

            openBrack = openStack.pop()
            if openBrack == "(" and bracket == ")":
                continue
            elif openBrack == "[" and bracket == "]":
                continue 
            elif openBrack == "{" and bracket == "}":
                continue
            else:
                return False
    
    if len(openStack) == 0:
        return True
    return False

s1 = "()"
print(valid_parentheses(s1))
#True

s2 = "()[]{}"
print(valid_parentheses(s2))
#True

s3 = "(]"
print(valid_parentheses(s3))
#False

s4 = "([)]"
print(valid_parentheses(s4))
#False

s5 = "{[[]()]}"
print(valid_parentheses(s5))
#True