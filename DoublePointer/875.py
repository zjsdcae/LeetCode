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
        j = piles[i]
        print(j)
        while j > 0:
            print(j)
            total = 0
            for pile in piles:
                total += pile//j + (pile%j>0)
            if total > H:
                break
            j -= 1
        return j+1

test = Solution()
test.minEatingSpeed([312884470],312884469)