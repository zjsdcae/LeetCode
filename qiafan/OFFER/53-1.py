class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        for n in nums:
            if n == target:
                res += 1
        return