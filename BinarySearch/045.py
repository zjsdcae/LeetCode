class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        if len(matrix[0]) == 0: return False
        leni,lenj = len(matrix),len(matrix[0])
        i,j = 0,lenj-1
        while i < leni:
            if matrix[i][j] == target: return True 
            if matrix[i][j] > target: break
            i += 1
        if i == leni: return False 
        if matrix[i][0] > target: return False
        l,r = 0,j 
        while l <= r:
            mid = (l+r) >> 1
            if matrix[i][mid] < target: l = mid + 1
            elif matrix[i][mid] > target: r = mid - 1
            else: return True
        return False