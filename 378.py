class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,length = [],len(matrix)
        for i in range(length):
            l += matrix[i]
        l.sort()
        return l[k-1]