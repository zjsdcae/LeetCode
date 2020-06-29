class Solution:
    def maxPoints(self, points):
        res = 0
        length = len(points)
        if length == 1:
            return 1
        for i in range(length-1):
            ss = {}
            samePoints = 0
            for j in range(i+1,length):
                grad = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) if points[j][0] != points[i][0] else "inf"
                if points[i] == points[j]:
                    samePoints += 1
                ss[grad] = ss.get(grad,1) + 1
            if max(ss,key=ss.get) != 0:
                temp = ss[max(ss,key=ss.get)] + samePoints
            else:
                temp = ss[max(ss,key=ss.get)]
            res = temp if temp > res else res
        return res

test = Solution()
print(test.maxPoints([[0,0],[0,0]]))

