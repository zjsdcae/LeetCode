class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        res,s = [],nums[0:k]
        res.append(max(s))
        i,length = k,len(nums)
        for i in range(k,length):
            s.pop(0)
            s.append(nums[i])
            res.append(max(s))
        return res
        # res = []
        # length = len(nums)
        # for i in range(length-k+1):
        #     res.append(max(nums[i:i+k]))
        # return res