class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.prefixSum =[]
        # cur= 0
        # for n in nums:
        #     cur+=n
        #     self.prefixSum.append(cur)
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        # rightSum = self.prefixSum[right]
        # leftSum = self.prefixSum[left-1] if left>0 else 0
        # return rightSum-leftSum
        Sum = 0
        for i in range(left, right+1):
            Sum += self.nums[i]
        return Sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)