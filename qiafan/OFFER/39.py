class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        length = len(nums)
        half = length // 2
        for i in range(length):
            val = nums[i]
            dic[val] = dic.get(val,0)+1
            if dic[val] > half:
                return val