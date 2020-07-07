# class Solution:
#     def findRepeatNumber(self, nums: List[int]) -> int:
#         temp = {}
#         for num in nums:
#             if temp.get(num,0) != 0:
#                 return num
#             else:
#                 temp[num] = 1

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num 
            else:
                s.add(num)