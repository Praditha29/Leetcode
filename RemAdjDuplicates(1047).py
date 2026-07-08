#LEETCODE PROBLEM 1047: Remove All Adjacent Duplicates In String

def removeDuplicates(s):
        stack = [] #Keep adding characters into this
        for char in s:
            if stack and stack[-1] == char: # Element in stack and the one before that element 
                stack.pop() # If same, do no add, just pop
            else:
                stack.append(char)
        return ''.join(stack) 

s = "abbcd"
print(removeDuplicates(s))  