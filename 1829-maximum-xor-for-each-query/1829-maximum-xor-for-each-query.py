class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        maxNum = (1 << maximumBit) - 1  # This is 2^maximumBit - 1, with all bits set to 1
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        result = []
        for num in reversed(nums):
            result.append(xor_sum ^ maxNum)
            xor_sum ^= num

        return result