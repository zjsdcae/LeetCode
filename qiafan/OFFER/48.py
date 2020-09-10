class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        temp,res = "",0
        for c in s:
            if c not in temp: temp += c 
            else: temp = temp[temp.index(c)+1:] + c 
            res = max(res,len(temp))
        return res