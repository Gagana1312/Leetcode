class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board), len(board[0])
        w= len(word)
        path = set()
        if m==1 and n==1:
            return board[0][0]==word

        def dfs(r, c, i):
            if i == w:
                return True

            if board[r][c]!= word[i]:
                return False
            
            if (r,c) in path:
                return False
            
            path.add((r,c))

            for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                
                row, col = r + i_off, c + j_off

                if 0 <= row < m and 0 <= col < n:
                    if dfs(row, col, i + 1):
                        return True
            
            path.remove((r,c))
            return False
        
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        return False
        