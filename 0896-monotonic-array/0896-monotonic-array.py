class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # if nums[-1]-nums[0]<0:
        #     nums.reverse()
        # for i in range(len(nums)-1):
        #     if not (nums[i]<=nums[i+1]):
        #         return False
        # return True
        inc, dec = True,True
        for i in range(len(nums)-1):
            if not (nums[i]<=nums[i+1]):
                inc = False
            if not (nums[i]>=nums[i+1]):
                dec = False
        return inc or dec
        
            

            

        