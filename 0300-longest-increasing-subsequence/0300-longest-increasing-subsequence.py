class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # l,r =0,1
        # res = []

        # while l<r and r<=len(nums):
        #     if nums[l]<nums[r]:
        #         nums.remove(nums[r])
        #         l+=1
        #         r+=1
        # return len(nums)

        LIS =[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        
        return max(LIS)

        #O(n^2)
        #

                
        