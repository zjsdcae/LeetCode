class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] < target: l = mid + 1
            if nums[mid] >= target: r = mid - 1
        return l