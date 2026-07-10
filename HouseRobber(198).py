# def rob(nums):
    
#     rob1 = 0 # Best house till two houses ago
#     rob2 = 0 # Best house till previous house

#     for money in nums:
#         newRob = max(rob1 + money, rob2)
#         rob1 = rob2
#         rob2 = newRob

#     return rob2

    
# nums = [2, 7, 9, 3, 1]
# print(rob(nums))


#ALTERNATE CODE
def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    max_money = [0] * len(nums)
    max_money[0] = nums[0]
    max_money[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        rob = nums[i] + max_money[i-2]
        skip = max_money[i-1]
        max_money[i] = max(rob, skip)

    return max_money[-1]

nums = [2,7,9,3,1]
print(rob(nums))