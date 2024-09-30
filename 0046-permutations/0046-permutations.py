class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # BackTracking
        # n= len(nums)
        # res,sol=[],[]

        # def dfs():
        #     if len(sol) == n:
        #         res.append(sol[:])
        #         return
            
        #     for i in nums:
        #         if i not in sol:
        #             sol.append(i)
        #             dfs()
        #             sol.pop()
        # dfs()
        # return res
#         if len(nums) == 0:
#             return [[]]
        
#         permutation =self.permute(nums[1:])
#         res = []
#         for p in permutation:
#             for i in range(len(p)+1):
#                 p_copy=p.copy()
#                 p_copy.insert(i,nums[0])
#                 res.append(p_copy)


#         return res
        
        # perms =[[]]

        # for n in nums:
        #     new_perms = []
        #     for p in perms:
        #         for i in range(len(p)+1):
        #             p_copy = p.copy()
        #             p_copy.insert(i,n)
        #             new_perms.append(p_copy)
        #     perms = new_perms
        # return perms




        # BackTracking
        n= len(nums)
        res,sol=[],[]

        def dfs():
            if len(sol) == n:
                res.append(sol.copy())
                return
            
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    dfs()
                    sol.remove(i)
        dfs()
        return res
         