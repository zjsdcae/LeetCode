class Solution:
    def cuttingRope(self, n: int) -> int:
        res,dp = 1,[0,1,1,2,4,6,9]
        if n <= 6:
            return dp[n]
        while n>6:
            res *= 3
            n -= 3
        return res * dp[n] % 1000000007