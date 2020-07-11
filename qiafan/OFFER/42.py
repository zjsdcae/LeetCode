class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = []
        dp.append(nums[0])
        for i in range(1,length):
            if dp[i-1]>=0:
                dp.append(dp[i-1]+nums[i])
            else:
                dp.append(nums[i])
        return max(dp)
        