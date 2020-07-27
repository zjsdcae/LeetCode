class Solution:
    def frequencySort(self, s: str) -> str:
        dic,res = {},""
        for c in s:
            dic[c] = dic.get(c,0)+1
        ss = sorted(dic.items(), key=lambda x:x[1], reverse = True)
        for c,n in ss:
            res += c*n
        return res