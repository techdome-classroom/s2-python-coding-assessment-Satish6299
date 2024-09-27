def isValid(s):
    # Dictionary to hold the matching pairs
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of open brackets
    stack = []
    
    # Traverse each character in the string
    for char in s:
        # If it's a closing bracket
        if char in matching_brackets:
            # Check the top of the stack, if stack is not empty, else set top_element to a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the top element doesn't match the corresponding open bracket, return False
            if matching_brackets[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it to the stack
            stack.append(char)
    
    # If the stack is empty, all brackets are matched correctly
    return not stack

# Example Test Cases:

# Example 1
s1 = "()"
print(isValid(s1))  # Output: True

# Example 2
s2 = "()[]{}"
print(isValid(s2))  # Output: True

# Example 3
s3 = "(]"
print(isValid(s3))  # Output: False







    



  

