def reverseWords(s):
    s.strip() #Remove spaces
    words = s.split() # into lists
    reversed_words = words[::-1] #Reverse the Words
    return ' '.join(reversed_words)

s = "a good   example"
print(reverseWords(s))