#LEETCODE PROBLEM 136: SINGLE NUMBER

def SingleNum(nums):

    result = 0 #comparing (XORing) every number with 0

    for num in nums: #iterate through every number in the list
        result ^= num #XOR with the result 
    return result #whatever the result is after XOR, store it here

nums = [4,1,2,1,2]
print(SingleNum(nums))
