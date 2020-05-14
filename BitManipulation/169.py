class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[int(len(nums)/2)]
        res = 0
        cnt = 0
        for item in nums:
            if item != res:
                cnt -= 1
                if cnt < 0:
                    res = item
                    cnt = 1
            else:
                cnt += 1
        return res
            
