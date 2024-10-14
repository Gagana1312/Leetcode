class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # score =0

        # for i in range(0,k+1):
        #     if 0<=i<len(nums):
        #         score+=nums[i]
        #         nums[i] = ceil(nums[i]//3)
        # return score
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            score += largest
            next_value = (largest + 2) // 3
            heapq.heappush(max_heap, -next_value)
        
        return score
                

            