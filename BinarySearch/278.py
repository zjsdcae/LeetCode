# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,res,r = 0,-1,n
        while l <= r:
            mid = (l+r) >> 1
            if !isBadVersion(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res