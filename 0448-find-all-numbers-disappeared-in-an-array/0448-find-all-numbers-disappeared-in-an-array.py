class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result =[]
        # n= len(nums)
        # for i in range(1,n+1):
        #     if i not in nums:
        #         result.append(i)
        # return result

        # for n in nums:
        #     i=abs(n)-1
        #     nums[i] = -1 * abs(nums[i])

        # res=[]
        # for i, n in enumerate(nums):
        #     if n>0:
        #         res.append(i+1)
        # return res
        count = Counter(nums)
        arr = []

        for i in range(1, len(nums)+1):
            if count[i] == 0:
                arr.append(i)
        return arr