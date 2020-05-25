def maxArea(height):
    # time exceeds
    # length = len(height)
    # i,j = 0,length-1
    # res = (j-i)*min(height[j],height[i])
    # if j-i <= 2:
    #     return max(min(height[j],height[i]),res)
    # else:
    #     return max(maxArea(height[i+1:j+1]),maxArea(height[i+1:j]),maxArea(height[i:j]),res)
    
    maxArea = 0
    i,j = 0,len(height)-1
    while i < j:
        area = min(height[i],height[j])*(j-i)
        leftValue = height[i]
        rightValue = height[j]
        if area > maxArea:
            maxArea = area;
        if(height[i]>height[j]):
            j -= 1
            while height[j] < rightValue:
                j -= 1
        else:
            i += 1 
            while height[i] < leftValue:
                i += 1
    return maxArea


    
test = [1,8,6,2,5,4,8,3,7]
print(maxArea(test))