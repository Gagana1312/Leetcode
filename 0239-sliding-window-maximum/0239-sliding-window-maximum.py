
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #time limit exceeded
        # ar = []
        # res =[]
        # left = 0
        # for right in range(k-1,len(nums)):
        #     for i in range(left, right+1):
        #         ar.append(nums[i])
        #     res.append(max(ar))
        #     left+=1
        #     ar= []
        
        # return res
        res =[]
        q = collections.deque()
        l=r=0

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            #remove left val from window
            if l > q[0]:
                q.popleft()

            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res







        