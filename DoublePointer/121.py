class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice,maxEarn = inf, 0
        for i in range(len(prices)):
            minPrice = min(minPrice,prices[i])
            maxEarn = max(maxEarn,prices[i]-minPrice)
        return maxEarn
        # if len(prices) == 0: return 0
        # res,l,r,length = 0,[prices[0]],[prices[-1]],len(prices)
        # for i in range(1,length): l.append(min(l[-1],prices[i]))
        # for j in range(length-2,-1,-1): r.append(max(r[-1],prices[j]))
        # r = r[::-1]
        # for i in range(length): res = max(res,r[i]-l[i])
        # return res