class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        length = len(nums)
        s = 0
        for i in range(length):
            if sortedNums[i] == nums[i]:
                continue
            s = i
            break
        if s == length-1:
            return 0 
        j = length-1
        while j > s:
            if nums[j] == sortedNums[j]:
                j -= 1 
                continue
            else:
                return j-s+1
        return 0 