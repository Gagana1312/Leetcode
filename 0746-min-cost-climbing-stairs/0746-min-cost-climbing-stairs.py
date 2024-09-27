class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        res=[0]*(n+1)
        if n==0:
            return 0
        if n==1:
            return cost[0]
        for i in range(2,n+1):
            res[i] = min(res[i-1]+cost[i-1], res[i-2]+cost[i-2])
        return res[-1]
            