class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        # for n in nums:
        #     x= n*n
        #     res.append(x)
        # res = sorted(res)
        # return res

        l,r = 0,len(nums)-1
        res =[]
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res.append(nums[l] ** 2)
                l+=1
            else:
                res.append(nums[r ]** 2)
                r-=1
        res.reverse()
        return res



        