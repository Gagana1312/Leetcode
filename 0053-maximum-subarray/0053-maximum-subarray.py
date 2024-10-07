class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = nums[0]
        # crsum = 0

        # for n in nums:
        #     if crsum<0:
        #         crsum=0
        #     crsum+=n
        #     res =max(res,crsum)
        # return res


        cur_sum =0
        output =float('-inf')

        for i in range(len(nums)):
            cur_sum+=nums[i]
            output = max(output, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return output

        