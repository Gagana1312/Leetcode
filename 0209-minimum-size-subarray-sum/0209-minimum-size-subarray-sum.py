class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        summ = 0
        min_len = float('inf')
        
        for r in range(len(nums)):
            summ += nums[r]
            
            while summ >= target:
                min_len = min(min_len, r - l + 1)
                summ -= nums[l]
                l += 1
        
        return min_len if min_len != float('inf') else 0
        
            
                
                


            

        