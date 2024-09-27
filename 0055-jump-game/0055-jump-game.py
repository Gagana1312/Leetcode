class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n= len(nums)
        # if n==0:
        #     return False
        # if n==1:
        #     return True
        # # if n==2:
        # #     return nums[0]==0 and nums[1]==1 or nums[0]==1
        
        # for i in range(n-1):
        #     jump = nums[i]
        #     for k in range(jump):
        #         if jump<n and nums[i+jump] == nums[-1]:
        #             return True
        # return False

        # n= len(nums)
        # memo = {n-1:True}
        # def can_reach(i):
        #     if i in memo:
        #         return memo[i]
            
        #     for jump in range(1, nums[i]+1):
        #         if can_reach(i+jump):
        #             memo[i] = True
        #             return True

        #     memo[i]= False
        #     return False
        # return can_reach(0)


        n= len(nums)
        target = n-1

        for i in range(n-1,-1,-1):
            jump = nums[i]
            if i+jump >=target:
                target=i
        return target==0



                

        