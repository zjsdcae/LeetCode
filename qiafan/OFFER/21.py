class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        length = len(nums)
        odd = []
        even = []
        for i in range(length):
            if nums[i]%2 == 1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        return odd+even