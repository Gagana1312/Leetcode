class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res =[]
        # prod=1
        # for i in range(len(nums)):
        #     for n in nums:
        #         prod *= n
        #     if nums[i] != 0:
        #         x = prod/ nums[i] 
        #     else:
        #         x=prod
        #     res.append(int(x))
        #     prod=1
        # return res

        res =[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]= prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*= postfix
            postfix *= nums[i]
        return res

