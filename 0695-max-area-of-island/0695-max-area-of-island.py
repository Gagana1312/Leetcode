class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        max_area =0

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1 :
                return 0
            else:
                grid[i][j]=0
                res = (1+ dfs(i+1,j)+ dfs(i,j+1)+ dfs(i-1,j)+ dfs(i,j-1))
                return res

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area = max(max_area, dfs(i,j))

        return max_area
