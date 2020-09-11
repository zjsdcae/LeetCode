class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) < 3: return max(nums)
        temp = [nums[0],nums[1],nums[0]+nums[2]]
        for i in range(3,len(nums)): temp.append(max(temp[i-2],temp[i-3])+nums[i])
        return max(temp)
