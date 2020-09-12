class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0,1,2]
        for _ in range(2,n): res.append(res[-1]+res[-2])
        return res[n]
