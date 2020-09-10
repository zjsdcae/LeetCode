class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        res = [-1,-1]
        if len(A) == 0: return res 
        for i in range(len(A)):
            if A[i] == target: 
                res[0] = i
                for j in range(i,len(A)):
                    if A[j] != target: 
                        res[1] = j - 1 
                        break
                if res[-1] == -1: res[1] = len(A)-1
                return res
        return res
                        
        # res = [-1,-1]
        # if len(A) == 0: return res
        # l,r = 0,len(A)-1
        # while l <= r:
        #     mid = (l+r) >> 1
        #     if A[mid] >= target: r = mid - 1 
        #     if A[mid] < target: l = mid + 1 
        # res[0] = l  
        # l,r = res[0],len(A)-1 
        # while l <= r:
        #     mid = (l+r) >> 1 
        #     if A[mid] <= target: l = mid + 1 
        #     if A[mid] > target: r = mid + 1 
        # res[1] = r
        # return res