class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # nums.sort()
        # return nums[len(nums)-k]
        nums = [-s for s in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -(heapq.heappop(nums))

        
        
        

        