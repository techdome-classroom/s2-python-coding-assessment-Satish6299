def setup(s):
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in matching_brackets:
            top_element = stack.pop() if stack else '#'
            if matching_brackets[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
s1 = "()"
print(isValid(s1)) 

s2 = "()[]{}"
print(isValid(s2))  


s3 = "(]"
print(isValid(s3)) 







    



  

