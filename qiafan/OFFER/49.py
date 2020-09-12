class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        a,b,c = 0,0,0
        for _ in range(n-1):
            temp = min(res[a]*2,res[b]*3,res[c]*5)
            if res[a]*2 == temp: a += 1
            if res[b]*3 == temp: b += 1
            if res[c]*5 == temp: c += 1
            res.append(temp)
        return res[-1]