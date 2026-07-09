def productExceptSelf(nums):
    answer = [1]
    # This is done to take the product of the right side
    for i in range(len(nums)-1, 0, -1): #start, stop, step
        answer.append(answer[-1] * nums[i]) # answer = [1,4,12,24]
    answer = answer[::-1] #Reverse the array. answer = [24,12,4,1]
    left = 1
    for i in range(len(nums)):
        answer[i] = answer[i] * left
        left *= nums[i]
    return answer


nums = [1,2,3,4]
print(productExceptSelf(nums))