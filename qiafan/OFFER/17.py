class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # res = []
        # i = 1
        # while (len(str(i))) <= n:
        #     res.append(i)
        #     i += 1
        # return res

        return list(range(1,10**n))