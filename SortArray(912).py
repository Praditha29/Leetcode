#LEETCODE PROBLEM 912: Sort an Array

#Bubble Sort Algorithm
# def sortArray(nums):
#         n = len(nums)
#         for i in range(n):
#             swapped = False
#             for j in range(0, n-i-1):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#                     swapped = True
#         return nums

# nums = [5,2,3,1]
# print(sortArray(nums))

#Merge Sort Algorithm
class Solution:
    def sortArray(self, nums):
        n = len(nums)
        temp = [0] * n
        size = 1

        while size < n:

            # Merge subarrays in pairs
            for left in range(0, n, 2 * size):

                mid = min(left + size - 1, n - 1)
                right = min(left + 2 * size - 1, n - 1)

                # Skip if there is only one subarray
                if mid >= right:
                    continue

                i = left       # pointer for left half
                j = mid + 1    # pointer for right half
                k = left       # pointer for temp array

                # Merge two sorted halves
                while i <= mid and j <= right:
                    if nums[i] <= nums[j]:
                        temp[k] = nums[i]
                        i += 1
                    else:
                        temp[k] = nums[j]
                        j += 1
                    k += 1

                # Copy remaining elements from left half
                while i <= mid:
                    temp[k] = nums[i]
                    i += 1
                    k += 1

                # Copy remaining elements from right half
                while j <= right:
                    temp[k] = nums[j]
                    j += 1
                    k += 1

                # Copy merged part back to nums
                for idx in range(left, right + 1):
                    nums[idx] = temp[idx]

            size *= 2

        return nums