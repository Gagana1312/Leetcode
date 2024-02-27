class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        l= 1

        for r in range(1,len(nums)):
            if nums[r]!= nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
        