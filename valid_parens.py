# lets think about the problem
# what data structures could we use?
# think back to data structures you have used for other problems
# think about if a loop or some nested logic would be a good fit
# think about possible valid items

def isValid(s):
    pass



# tests
print(isValid("()")) # => True
print(isValid("()[]{}")) # => True
print(isValid("(]")) # => False
print(isValid("([)]")) # => False
print(isValid("{[]}")) # => True
print(isValid("")) # => True

