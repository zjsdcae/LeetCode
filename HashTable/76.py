class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic,dictarget,res = {},{},s
        lens, lent = len(s), len(t)
        for i in range(lent):
            dictarget[t[i]] = dictarget.get(t[i],0) + 1
        for i in range(lens):

        # if s == t: return s
        # dic,res = {},s
        # lens,lent = len(s),len(t)
        # for i in range(lens):
        #     if s[i] in t:
        #         dic[s[i]] = i
        #         if len(dic) == lent:
        #             temp = sorted(dic.values())
        #             dis = temp[-1]-temp[0]+1
        #             if dis <= len(res):
        #                 res = s[temp[0]:temp[-1]+1]
        # if len(dic) == len(t):
        #     return res
        # else:
        #     return ""