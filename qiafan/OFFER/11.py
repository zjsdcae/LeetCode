class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        for i in range(1,length):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]