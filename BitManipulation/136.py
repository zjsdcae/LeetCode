class Solution:
    def singleNumber(self, nums: List[int] ) -> int:
        res = 0
        for item in nums:
            res = res ^ item
        return res

# return sum(set(nums))*2 - sum(nums)
