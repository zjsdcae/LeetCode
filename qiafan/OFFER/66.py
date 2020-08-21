class Solution:
    def constructArr(self, a):
        i,length,res = 1,len(a),[]
        ll, rl = [1],[1]        
        while i < length:
            ll.append(a[i-1]*ll[-1])
            i += 1
        while i > 1:
            i -= 1
            rl.append(a[i]*rl[-1])
        rl = rl[::-1]
        for i in range(length):
            res.append(ll[i]*rl[i])
        return res