class Solution:
    def minEatingSpeed(self, piles, H):
        piles.sort()
        length = len(piles)
        minPile = piles[length-1]
        for i in range(length):
            total = 0
            for pile in piles:
                total += pile//piles[i] + (pile%piles[i]>0)
            if total < H:
                break

        l,h = 1,piles[i]
        while l<h:
            m = (l+h)//2
            total = 0
            for pile in piles:
                total += pile//m + (pile%m>0)
            if total <= H:
                h = m
            else:
                l = m+1
        return l
