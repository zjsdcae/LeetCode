class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,res,length = 0,0,len(s)
        while i < length:
            temp = []
            j = i
            while j < length and s[j] not in temp:
                temp.append(s[j])
                j += 1
            lengthTemp = len(temp)
            if lengthTemp > res:
                res = lengthTemp
            i = j
        return res