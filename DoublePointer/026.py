class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j,length = 0,1,len(nums)
        while j < length:
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1