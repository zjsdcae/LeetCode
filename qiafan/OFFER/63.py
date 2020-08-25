class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j,res = 0,1,0
        if len(prices) <= 1: return 0
        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j
            else:
                res = max(res,prices[j]-prices[i])
            j += 1
        return res
        # timeout
        # res,length = 0,len(prices)
        # if length == 0: return 0
        # temp = prices[0]
        # for i in range(length):
        #     if prices[i] > temp:
        #         continue
        #     for v in prices[i:length]:
        #         if v - prices[i] > res:
        #             temp = prices[i]
        #             res = v - prices[i]
        # return res
        # res,length = 0,len(prices)
        # i,j = 0,length-1
        # while i < j:
        #     temp = prices[j] - prices[i]
        #     if temp > res:
        #         res = temp
        #     tempi,tempj = prices[i],prices[j]
        #     while i < j and prices[i+1] > tempi:
        #         i += 1
        #     if i != tempi : continue
        #     while j > i and prices[j-1] < tempj:
        #         j -= 1

        # return res
