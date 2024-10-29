class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(row, col):
            if memo[row][col] != -1:
                return memo[row][col]
            
            max_move = 0
            # Possible moves to the right (up, right, down)
            for dr in [-1, 0, 1]:
                new_row = row + dr
                new_col = col + 1
                if 0 <= new_row < m and new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_move = max(max_move, 1 + dfs(new_row, new_col))
            
            memo[row][col] = max_move
            return max_move

        max_result = 0
        for i in range(m):
            max_result = max(max_result, dfs(i, 0))
        
        return max_result