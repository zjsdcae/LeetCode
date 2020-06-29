class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        expected = (1+length)*length/2
        current = sum(nums)

        s = set()
        for i in range(length):
            if nums[i] in s:
                duplicated = nums[i]
                break
            s.add(nums[i])
        
        lost = int(duplicated + (expected-current))
        return [duplicated,lost]