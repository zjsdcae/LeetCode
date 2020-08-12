class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = ['a','e','i','o','u']
        res,temp,length = 0,0,len(s)
        for i in range(k):
            if s[i] in l:
                res += 1
        temp = res    
        for j in range(k,length):
            if s[j-k] in l: temp -= 1
            if s[j] in l: temp += 1
            if temp > res:
                res = temp
        return res
