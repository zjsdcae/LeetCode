class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0 
        leni,lenj = len(matrix),len(matrix[0])
        maxSide = 0
        temp = [[0]*lenj for _ in range(leni)]
        for i in range(leni):
            for j in range(lenj):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0: temp[i][j] = 1
                    else: temp[i][j] = min(temp[i-1][j],temp[i][j-1],temp[i-1][j-1])+1
                    maxSide = max(maxSide,temp[i][j])
        return maxSide ** 2