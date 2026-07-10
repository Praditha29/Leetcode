def MergeStringsAlternately():
    A, B = len(word1) , len(word2) #Taking length of both the words
    a, b = 0, 0 #Assigning index (acts like pointers)
    s = [] #To add each letters one by one here 

    word = 1 # for word 1. This will flip flop between 1 and 2
    while a < A and b < B: #check if the length is smaller than the index. 
        if word == 1:
            s.append(word1[a]) #add letter which is at a
            a += 1 #move a by one letter ahead
            word = 2 #go to word 2

        #same logic repeats for second word
        if word == 2:
            s.append(word2[b])
            b += 1
            word = 1

    while a < A: #If the word has extra length than the second word
        s.append(word1[a])
        a += 1

    while b < B:
        s.append(word2[b])
        b += 1

    return "".join(s) #s is now in the form of list, it is like:
# s = ["a", "x", "b", "y", "c", "z"]
# .join joins them all into a string

word1 = "abckjkjsh"
word2 = "xyzpq"
print(MergeStringsAlternately())