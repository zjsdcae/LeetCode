def sortColors(nums):
    length = len(nums)
    left, right, curr = 0, length-1, 0
    while curr < length:
        if curr == 1:
            curr += 1
        elif curr == 2:
            nums[right], nums[curr] = nums[curr], nums[right]
            right -= 1
        else:
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
    

