class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp,res = "",0
        for c in s:
            if c in temp:
                temp = temp[temp.index(c)+1:]
                temp += c
            else:
                temp += c
                res = max(res,len(temp))
        return res
