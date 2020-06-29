class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        contain,i,j = 0,0,length-1
        while i < j :
            if height[i] <= height[j]:
                volume = height[i]*(j-i)
                i += 1
            else:
                volume = height[j]*(j-i)
                j -= 1
            if volume > contain:
                contain = volume
        return contain
