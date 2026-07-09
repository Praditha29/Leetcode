#LEETCODE PROBLEM 9: PALINDROME NUMBER

def Palindrome(x):

    if x < 0: #Eliminate negative no case scenario as -ve number is never palindrome
        return False
    
    s = str(x) # Convert integer into string because pointers don't work on integers

    left = 0 #left pointer
    right = len(s) - 1 #indexing starts from 0 but length starts from 1. So -1

    while left < right: #so that the loop stops after crossing each other or in same place 
        if s[left] != s[right]: #if the element in this index is not same that means it is not palindrome
            return False
        left += 1
        right -= 1
    return True

x = 121
print(Palindrome(x))
