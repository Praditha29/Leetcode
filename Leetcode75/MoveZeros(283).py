#LEETCODE PROBLEM 283: MOVE ZEROS 

# left and right are the pointers 
# right moves forward as it is in the for loops and it iterates through every element
# left will only move forward when it is swapped 

def MoveZeros(nums):

    left = 0
    length = len(nums) #kyuki utna iterate krna hai 

    for right in range(length): # coz i need to check every element. 0,1,2,3,4
        if nums[right] != 2: 
            nums[right], nums[left] = nums[left], nums[right] # [] has index number and since nums[] is written, the elements are swapped
            # nums[right], nums[left] = 0,1 
            left += 1 #only moves forward when swapping is done

    return nums # returns the swapped list

nums = [2,1,3,12]
print(MoveZeros(nums)) #to send the list to the function
#---------------------------------------------------------------------------------------------------------------------#