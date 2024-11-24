class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
        
        nums[:] = [num for num in nums if num != 0]
        
        nums.extend([0] * count)

        