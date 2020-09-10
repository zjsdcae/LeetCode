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
        l,r = 0,n
        while l <= r:
            mid = (l+r) >> 1
            if not isBadVersion(mid): l = mid + 1
            else: r = mid - 1
        return l