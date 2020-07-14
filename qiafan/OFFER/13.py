class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sumBits(n):
            res = 0
            while n:
                res += n%10
                n //= 10
            return res
        res = 1
        temp = [[0 for i in range(n+1)] for i in range(m+1)]
        temp [1][1] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if sumBits(i)+sumBits(j)<=k and (temp[i][j+1] or temp[i+1][j]):
                    res += 1
                    temp[i+1][j+1] = 1
                    continue
        return res

