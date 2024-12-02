class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) 
        row_sum = [tuple(grid[row]) for row in range(m)]  
        col_sum = [tuple(grid[row][col] for row in range(m)) for col in range(n)]  
        
        
        res = 0
        row_set = set(row_sum)  
        for col in col_sum:
            if col in row_set:
                res += row_sum.count(col) 
                
        return res         




        
        