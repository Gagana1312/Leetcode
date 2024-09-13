class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            x= n*n
            res.append(x)
        res = sorted(res)
        return res

        