def reverseWords(s):
    s.strip()
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

s = "a good   example"
print(reverseWords(s))