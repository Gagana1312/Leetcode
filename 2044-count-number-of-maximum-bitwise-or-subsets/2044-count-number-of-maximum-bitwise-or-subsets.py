class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0  # Maximum OR value
        count = 0   # Number of subsets with maximum OR

        # Find the maximum possible OR value by OR-ing all elements
        for num in nums:
            max_or |= num

        # Helper function to count subsets with the maximum OR
        def backtrack(index, current_or):
            if index == len(nums):
                # If this subset's OR is equal to the maximum OR, increment count
                return 1 if current_or == max_or else 0

            # Count including the current element
            include = backtrack(index + 1, current_or | nums[index])
            # Count excluding the current element
            exclude = backtrack(index + 1, current_or)

            return include + exclude

        # Start backtracking from index 0 with an initial OR value of 0
        return backtrack(0, 0)