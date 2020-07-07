class Solution:
    def fib(self, n: int) -> int:
        a = [0,1]
        if n == 0 or n ==1:
            return a[n]
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        return a[-1]