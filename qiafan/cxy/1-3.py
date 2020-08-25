class Solution:
    def getv(self, s):
        last = s.pop()
        if not s:
            return last
        else:
            res = self.getv(s)
            s.append(last)
            return res

    def reverse(self,s):
        if not s:
            return 
        v = self.getv(s)
        self.reverse(s)
        s.append(v)
    
n = input()
s = []
test = Solution()
numArray = input()
for i in numArray.split():
    s.append(int(i))
test.reverse(s)
print(' '.join(str(i) for i in s))
            