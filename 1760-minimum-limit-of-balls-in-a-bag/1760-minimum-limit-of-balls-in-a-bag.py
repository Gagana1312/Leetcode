class Solution(object):
    def check(self, nums, maxOperations, penalty):
        ops = 0
        for num in nums:
            ops += (num - 1) // penalty
        return ops <= maxOperations

    def minimumSize(self, nums, maxOperations):
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            if self.check(nums, maxOperations, mid):
                right = mid
            else:
                left = mid + 1

        return left
        