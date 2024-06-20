class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        crsum = 0

        for n in nums:
            if crsum<0:
                crsum=0
            crsum+=n
            res =max(res,crsum)
        return res

        