class Solution:
    def apnd(self, l, num):
        res = []
        for item in l:
            item.append(num)
            res.append(item)
        return res

    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res += self.apnd(res,num)
        return res