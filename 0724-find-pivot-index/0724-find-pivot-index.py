class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total = sum(nums)
        # leftSum=0
        # for i in range(len(nums)):
        #     rightSum = total -nums[i]-leftSum
        #     if leftSum ==rightSum:
        #         return i
        #     leftSum+=nums[i]
        # return -1
        for i in range(len(nums)):
            sumLeft = sum(nums[:i])
            sumRight = sum(nums[i+1:])
            if sumLeft == sumRight:
                return i
        return -1
       


