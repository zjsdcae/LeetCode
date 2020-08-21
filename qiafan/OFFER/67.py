class Solution:
    def strToInt(self, str: str) -> int:
        i,flag,length,res = 0,1,len(str),0
        if length == 0: return 0
        while i < length:
            if str[i] == ' ': 
                i += 1
                continue
            if not str[i].isdigit() and str[i] != '-' and str[i] != '+': return 0
            if str[i].isdigit() or str[i] == '-' or str[i] == '+':
                if str[i] == '-' or str[i] == '+': 
                    if str[i] == '-': flag = -1
                    i += 1
                if i >= length: break
                while i<length and str[i].isdigit():
                    res = res * 10 + int(str[i])
                    i += 1
                result = res*flag
                if result >= 2 ** 31: return 2**31 -1
                if result < -2 ** 31: return -2**31 
                return result
            i += 1
        return 0
