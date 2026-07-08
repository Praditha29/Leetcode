#LEETCODE PROBLEM 1431: KIDS WITH THE GREATES NUMBER OF CANDIES
def kidsWithCandies(candies, extraCandies):

    greatest = max(candies) # Get the max number to compare with
    result = [] # store result in list
    
    for candy in candies:
        if candy + extraCandies >= greatest:
           result.append(True)
        else:
           result.append(False)
    return result

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))