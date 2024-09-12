class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0,10000000):
        #     for n in nums:
        #         if n == i:
        #             return n
        # return 0

        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
    

        