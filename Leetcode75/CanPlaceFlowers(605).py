def canPlaceFlowers(flowerbed, n):
    if n == 0: # if no flowers are to be placed
        return True
    
    for i in range(len(flowerbed)):
        # when i (index) is 0, left automatically is 0, 
        left = (i == 0) or (flowerbed[i-1] == 0) # check if anything to the left is there or not if it is there then is it empty or not
        # when last index is 0, it means the pointer is to the last index so nothing is after last one
        right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) #same as what we did to left
        if left and right and flowerbed[i] == 0: #if all three are true
            flowerbed[i] = 1 # mark the current index where the loop is to one
            n -= 1 
            if n == 0: # goes on till n is 0
                return True
    return False

#Test case:
flowerbed = [1,0,0,0,1]
n = 0
print(canPlaceFlowers(flowerbed, n))