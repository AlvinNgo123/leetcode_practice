def valid_parentheses(s):
    pass

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