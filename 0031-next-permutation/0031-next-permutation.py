class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the pivot
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        if pivot == -1:
            # If no pivot found, this is the last permutation
            nums.reverse()
            return
        
        # Step 2: Find the successor
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                # Step 3: Swap
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        # Step 4: Reverse the suffix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        """
        Do not return anything, modify nums in-place instead.
        """
        
        