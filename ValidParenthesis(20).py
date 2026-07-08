#LEETCODE PROBLEM 20: Valid Parentheses

def isValid(s):
        stack = [] # Empty now. Will append if key is not found in the test case
        mapping = {')':'(', '}':'{', ']':'['} 
        for char in s: # for each element in the test case
            if char in mapping: #Check if the character is in the dict mapping
                top = stack.pop() if stack else '#' #if yes then remove the top element from the stack
                if mapping[char] != top: #if the character matched but it is not on top of stack, then return False. Doesn't matter if it is present in the stack
                    return False
            else:
                stack.append(char) #if character is not in the key of dict, put it in the stack. 
        return not stack

s = "({[]})"
print(isValid(s))  # Output: True

#check and match each element of the test case with dictionary mapping. If the character is not in the dict as a key, put that char in 
# the stack. If the character matches, remove the last element (top char) present in the stack. If after checking everything, the stack is 
#empty, that means that the test case is a valid parenthesis and will return true.