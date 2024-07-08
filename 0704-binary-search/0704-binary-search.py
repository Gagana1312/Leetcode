class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n)
        # if target not in nums:
        #     return -1
        
        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         return i
        # return
        
        #(O(logn))
        start, end = 0, len(nums)-1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid - 1
        return -1


            
        



        