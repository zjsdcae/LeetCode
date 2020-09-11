class Solution:
    def trap(self, height):
        if not height: return 0
        leftMax,rightMax,length = [height[0]],[height[-1]],len(height)
        for i in range(1,length): leftMax.append(max(height[i],leftMax[-1]))
        for j in range(length-2,-1,-1): rightMax.append(max(height[j],rightMax[-1]))
        rightMax = rightMax[::-1]
        res = 0
        for i in range(length):
            temp = min(leftMax[i],rightMax[i])-height[i]
            if temp > 0: res += temp
        return res

#         i,length,res = 0,len(height),0
#         dic = {}
#         while i < length-1:
#             j = i+1
#             while j < length:
#                 if height[j] < height[i]:
#                     dic[j] = height[j]
#                     j += 1
#                 else:
#                     break
#             if j == length and height[j-1]<height[i]:
#                 maxRight = max(dic, key=dic.get)
#                 j = maxRight
#             volume = (j-i-1)*min(height[j],height[i])
#             i += 1
#             while i < j:
#                 volume -= height[i]
#                 i += 1
#             res += volume
#             dic.clear()
#         return res
