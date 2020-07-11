class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,v in enumerate(nums):
            if v in dic:
                return [v,dic[v]]
            dic[target-v] = v
            