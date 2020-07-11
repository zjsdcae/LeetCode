class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        zero = 0
        temp = []
        for num in nums:
            if num == 0:
                zero += 1
                continue
            temp.append(num)
        if zero == 5 or zero == 4:
            return True
        s = sorted(temp)[::-1]
        length = len(s)
        minus = 0
        for i in range(length-1):
            if s[i] == s[i+1]:
                return False
            minus += s[i]-s[i+1]
        return True if minus-length+1-zero <= 0 else False