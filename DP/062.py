# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        # else:
        #     return self.uniquePaths(m-1 ,n)+self.uniquePaths(m, n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0]*(m+1) for _ in range(n+1)]
        path[1][1] = 1
        i,j = 1,2
        while i < n+1:
            while j < m+1:
                path [i][j] = path[i-1][j] + path[i][j-1]
                j += 1
            j = 1
            i += 1
        return path[n][m]