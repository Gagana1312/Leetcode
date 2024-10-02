class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_linear(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
            return dp[-1]
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

        






















    
    #     return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        
    
    # def helper(self, nums):
    #     r1,r2 =0,0
    #     for n in nums:
    #         newRob = max(r1+n, r2)
    #         r1= r2
    #         r2 = newRob
    #     return r2
