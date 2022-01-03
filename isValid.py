#Runtime: O(n) | Space: O(n)
def isValid(s: str) -> bool:
    #Go through string char by char
    #Each char, see if its an opening or closing bracket
        #If opening, push it onto the stack
        #if closing, pop top element from stack and see if its corresponding open
            #If yes, continue
            #If no, return false
    #If we make it to the end and out stack is empty, we know it's valid so return true. Else, return false.
    brackStack = [] 
    openBracks = ['[', '{', '(']

    for brack in s:
        if brack in openBracks:
            brackStack.append(brack)
        else:
            if len(brackStack) != 0:
                topOpen = brackStack.pop()
                if topOpen == '[' and brack == ']':
                    continue
                elif topOpen == '{' and brack == '}':
                    continue
                elif topOpen == '(' and brack == ')':
                    continue
                else:
                    return False
            else:
                return False
    
    if len(brackStack) == 0:
        return True
    else:
        return False
            

s = "()"
print(isValid(s))
#True

s = "()[]{}"
print(isValid(s))
#True

s = "(]"
print(isValid(s))
#False

s = "()[{]}"
print(isValid(s))
#False because closed in incorrect order