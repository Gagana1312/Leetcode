class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            j = bisect_left(nums, lower - x, lo=i + 1)
            k = bisect_left(nums, upper - x + 1, lo=i + 1)
            ans += k - j
        return ans