class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res,sol=[],[]

        def dfs(x):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            left = x
            still_need = k - len(sol)

            if left > still_need:
                dfs(x - 1)

            sol.append(x)
            dfs(x - 1)
            sol.pop()
            
        dfs(n)
        return res
        