#LEETCODE PROBLEM 26: Remove Duplicates from Sorted Array

def removeDuplicates(nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow +1

nums = [1,1,2,2,3]
k = removeDuplicates(nums) #k stores unique elements from removeDuplicates function
print(nums[:k]) #coz only the first 3 elements count and that's stored in k