class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1: return 0
        leni,lenj = len(grid),len(grid[0])
        def dfs(i,j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for x,y in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                    if not 0 <= x < leni or not 0 <= y < lenj:
                        continue 
                    else:
                        dfs(x,y)
            return 
        res = 0
        for i in range(leni):
            for j in range(lenj):
                if grid[i][j] == '1': 
                    res += 1
                    dfs(i,j)
        return res