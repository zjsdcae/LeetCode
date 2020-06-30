class Solution:
    def trap(self, height):
        i,length,res = 0,len(height),0
        dic = {}
        while i < length-1:
            j = i+1
            while j < length:
                if height[j] < height[i]:
                    dic[j] = height[j]
                    j += 1
                else:
                    break
            if j == length and height[j-1]<height[i]:
                maxRight = max(dic, key=dic.get)
                j = maxRight
            volume = (j-i-1)*min(height[j],height[i])
            i += 1
            while i < j:
                volume -= height[i]
                i += 1
            res += volume
            dic.clear()
        return res
