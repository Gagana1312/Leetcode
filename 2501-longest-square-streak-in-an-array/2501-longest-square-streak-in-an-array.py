class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))  # Remove duplicates and sort
    
        num_set = set(nums)  # Set for O(1) lookups
        max_streak = 0

        for num in nums:
            current = num
            count = 1  # Starting with the first element

            while current in num_set:
                current = current ** 2  # Move to the next square
                if current in num_set:
                    count += 1

            if count >= 2:
                max_streak = max(max_streak, count)

        return max_streak if max_streak >= 2 else -1
