class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def longest_increasing_subsequence(arr):
            from bisect import bisect_left
            lis = []
            for num in arr:
                pos = bisect_left(lis, num)
                if pos == len(lis):
                    lis.append(num)
                else:
                    lis[pos] = num
            return len(lis)

        n = len(nums)
        if n < 3:
            return n  # Can't form a mountain array
        
        # Step 1: Compute LIS and LDS
        lis = [0] * n
        lds = [0] * n
        
        for i in range(n):
            lis[i] = longest_increasing_subsequence(nums[:i + 1])
        
        for i in range(n - 1, -1, -1):
            lds[i] = longest_increasing_subsequence(nums[i:][::-1])
        
        # Step 2: Find the maximum mountain array length
        max_length = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # Must have increasing and decreasing
                max_length = max(max_length, lis[i] + lds[i] - 1)
        
        # Step 3: Minimum removals
        return n - max_length
        