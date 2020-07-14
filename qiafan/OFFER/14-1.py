class Solution:
    def cuttingRope(self, n: int) -> int:
        l = [0,1,2,4,6,9]
        if n < 7:
            return l[n-1]
        for i in range(7,n+1):
            l.append(3*l[i-4])
        return l[-1]