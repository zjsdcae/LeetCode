class Solution:
    def countPrimes(self, n: int) -> int:
        res,resList = 0,[True]*n
        for i in range(2,n):
            if resList[i]:
                res += 1
                j = i*i
                while j < n:
                    resList[j] = False
                    j += i
        return res