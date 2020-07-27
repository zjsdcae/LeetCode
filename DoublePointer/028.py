class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        length,lenn = len(haystack),len(needle)
        for i in range(length-lenn+1):
            if haystack[i] == needle[0] :
                j = i
                if lenn == 1:
                    return i
                for c in needle[1:]:
                    if haystack[j+1] == c:
                        j += 1
                        continue
                    else: break
                if j == i + lenn - 1 :
                    return i
            i += 1
        return -1