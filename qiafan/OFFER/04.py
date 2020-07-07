class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        try:
            n = len(matrix)
            m = len(matrix[0])
            if target < matrix[0][0]:
                return False
        except Exception:
            return False
        
        i,j = 0,m-1
        while j>0 :
            if matrix[0][j] <= target: 
                break
            j -= 1
        while i<n-1:
            if matrix[i][j] >= target:
                break
            i += 1
        for a in range(i,n):
            for b in range(j+1):
                if matrix[a][b] == target:
                    return True
        return False