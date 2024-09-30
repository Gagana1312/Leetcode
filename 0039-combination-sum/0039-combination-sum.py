class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res,sol=[],[]
        nums = candidates
        n= len(nums)

        def dfs(i, cur_summ):
            if cur_summ == target:
                res.append(sol[:])
                return
            
            if cur_summ > target or i==n:
                return

            dfs(i+1,cur_summ)
            sol.append(nums[i])
            dfs(i,cur_summ+nums[i])
            sol.remove(nums[i])
        dfs(0,0)
        return res




















        # res = []

        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur[:])
        #         return
            
        #     if i >= len(candidates) or total > target:
        #         return

        #     cur.append(candidates[i])
        #     dfs(i, cur, total + candidates[i])
        #     cur.pop()
        #     dfs(i + 1, cur, total)

        # dfs(0, [], 0)
        # return res
        