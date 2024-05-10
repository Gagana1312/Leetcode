class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maj=0
        # l,r = 0, len(nums)-1
        # for i in range(len(nums)):
        #     maj = nums[r]/2
        #     maj = max(maj, nums[i])
        # return maj

        # res, maxCount = 0,0
        # count={}

        # for i in nums:
        #     count[i]=1+ count.get(i,0)
        #     res = i if count[i]>maxCount else res
        #     maxCount = max(count[i], maxCount)
        # return res

        # hashMap = {}
        # res, count=0, 0
        # for n in nums:
        #     if count == 0:
        #         res = n
        #     count+=(1 if n == res else -1)
        # return res

        maj=0
        for i in nums:
            if i!=maj:
                if nums.count(maj)<nums.count(i):
                    maj=i
        return maj



        