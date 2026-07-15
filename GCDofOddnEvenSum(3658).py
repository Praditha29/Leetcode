def gcdOfOddEvenSums(n):
    sumOdd = 0
    sumEven = 0

    # For odd numbers
    count = 0 # To keep track of how many numbers are taken 
    i = 1 # Iterate each number 
    while count < n: # Stop when we don't want more odd numbers than the count mentioned. If 4, it should be 1,3,5,7. No more than that
        sumOdd += i # add number to our sum 
        i += 2 
        count += 1

    # For even Numbers
    count = 0
    i = 2
    while count < n:
        sumEven += i 
        i += 2
        count += 1
    
    # GCD logic
    while sumEven:
        sumOdd, sumEven = sumEven, (sumOdd % sumEven)
    
    return sumOdd

# The common divisors of 20 and 16 are exactly the same as the 
# common divisors of 16 and the remainder when 20 is divided by 16 (which is 4)

n = 5
print(gcdOfOddEvenSums(n))