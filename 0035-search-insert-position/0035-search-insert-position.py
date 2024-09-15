class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        n= len(nums)
        end = n-1
        while start<=end:
            mid = (start+end) // 2
            if nums[mid]>target:
                end = mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                return mid
        if nums[mid]<target:
            return mid+1
        else:
            return mid
        # n = len(nums)
        # l = 0
        # r = n - 1

        # while l <= r:
        #     m = (l + r) // 2
            
        #     if nums[m] < target:
        #         l = m + 1
        #     elif nums[m] > target:
        #         r = m - 1
        #     else:
        #         return m

        # if nums[m] < target:
        #     return m + 1
        # else:
        #     return m

            

        