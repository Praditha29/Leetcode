# LEETCODE PROBLEM 1: TWOSUM

list1 = [2,11,7,15] # will stop once it finds a pair. Doesn't matter if the another is a pair after this or not
target = 9
def TwoSum(list1, target):
    seen = {} # Empty dictionary where we will be adding values and indexes which we came across
    
    for index, value in enumerate(list1): # value is element in the list 
        find_another = target - value # 
        if find_another in seen:
            return [seen[find_another], index]
        seen[value] = index

    return[]
print(TwoSum(list1, target))

 