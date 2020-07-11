class Solution:
    def firstUniqChar(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return " "
        dic = {}
        for i in range(length):
            dic[s[i]] = dic.get(s[i],0)+1
        for k in dic.keys():
            if dic[k] == 1:
                return k
        return " "
        