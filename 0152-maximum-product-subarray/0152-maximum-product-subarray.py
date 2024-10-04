class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = max(nums) 
        curmin, curmax = 1,1

        for n in nums:
            if n==0:
                curmin, curmax=1,1
                continue
            
            tmp = curmax*n
            
            curmax = max(n*curmax, n*curmin,n)
            curmin = min(tmp, n*curmin,n)
            res = max(res, curmax)
        return res


        