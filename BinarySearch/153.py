class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]
        l,r = 0,len(nums)-1
        if nums[0] < nums[r]: return nums[0]
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[mid] < nums[mid-1]: return nums[mid-1]
            if nums[mid] > nums[0]: l = mid + 1
            else: r -= 1