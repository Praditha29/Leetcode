def reverseVowels(s):
    s = list(s) #to work with index values. You can't do that with string
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
    return ''.join(s)

s = "leetcode"
print(reverseVowels(s))
