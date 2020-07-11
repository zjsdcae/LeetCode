class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] != i:
                return i 
        return nums[-1]+1