def increasingTriplet(nums):
        num_i = num_j = float('inf') #initially infinity so any number is smaller than this
        for num in nums:
            if num <= num_i: # If num is smaller than num_i
                num_i = num # Assign the value to num_i
            elif num <= num_j: # If num is not smaller than num_i but is not larger than num_j
                num_j = num # Assign the value to num_j
            else: 
                return True # If not smaller than num_i and num_j, then that means it is the biggest number so it will be k
                            #so instead of assigning it another variable, we can simply return True
        return False 
# False would mean that we did not find our k and it is not a Triplet.