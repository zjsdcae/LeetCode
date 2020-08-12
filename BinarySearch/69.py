class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        l,r = 0,x
        mid = (l+r) >> 1
        while l <= r :
            if mid ** 2 == x: return mid
            if mid ** 2 > x: r = mid - 1
            if mid ** 2 < x: l = mid + 1
            mid = (l+r) >> 1
        return mid