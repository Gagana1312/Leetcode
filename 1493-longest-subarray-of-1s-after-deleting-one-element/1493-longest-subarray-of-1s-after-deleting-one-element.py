class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numzeros = 0
        l = 0
        max_length = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                numzeros += 1

            while numzeros > 1:
                if nums[l] == 0:
                    numzeros -= 1
                l += 1
            max_length = max(max_length, r - l)
        return max_length


        