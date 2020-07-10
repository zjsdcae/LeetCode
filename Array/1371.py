class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        st = {'a','e','i','o','u'}
        dic = {}
        temp = []
        i = 0
        for char in s:
            if char in st:
                i += 1
                temp.append(i)
                dic[cahr] = dic.get(char,0)+1
                continue
            temp.append(i)
        
