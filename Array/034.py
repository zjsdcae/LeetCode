def searchRange(nums, target):
    res = [-1,-1]
    length = len(nums)
    left,right = 0,length-1
    i = int(right/2)
    while left <= right:
        i = (left+right)//2
        if nums[i] > target:
            right = i-1
        elif nums[i] < target:
            left = i+1
        else:
            leftRes,rightRes = i,i
            while nums[leftRes] == target and leftRes >= 0:
                leftRes -= 1
            res[0] = leftRes+1
            while rightRes <= length-1 and nums[rightRes] == target:
                rightRes += 1
                if rightRes == length-1 and nums[rightRes] == target:
                    rightRes += 1
                    break
            res[1] = rightRes-1
            return res
    return res

nums = [1,2,2,2,3]
print(searchRange(nums,2))
               