from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minutes=-1
        numfresh =0
        empty, fresh, rotten = 0,1,2
        m,n = len(grid), len(grid[0])
        q= deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    q.append((i,j))
                elif grid[i][j]==fresh:
                    numfresh+=1
        
        if numfresh ==0:
            return 0
        while q:
            q_size= len(q)
            minutes+=1
            for _ in range(q_size):
                i,j = q.popleft()
                for r, c in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]== fresh:
                        grid[r][c]= rotten
                        numfresh-=1
                        q.append((r,c))

        if numfresh==0:
            return minutes
        else:
            return -1




























        # m,n = len(grid), len(grid[0])
        # visited = set()
        # minutes =0

        # def dfs((i,j),(p,q), minutes):
        #     if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1' or grid[i][j]!='2':
        #         return
        #     elif grid[i][j]=='1':
        #         grid[i][j] = '2'
        #         minutes+=1
        #         dfs(i+1,j, minutes)
        #         dfs(i,j+1, minutes)
        #         dfs(i-1,j, minutes)
        #         dfs(i,j-1, minutes)
        #     else:
        #         dfs(i+1,j, minutes)
        #         dfs(i,j+1, minutes)
        #         dfs(i-1,j, minutes)
        #         dfs(i,j-1, minutes)

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]== '1' or grid[i][j]=='2':
        #             dfs(i,j, minutes)
        # return minutes



            

        