class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        max_combination_size = 0
    
        # We check all bits from 0 to 23 (because 10^7 fits in 24 bits)
        for bit in range(24):  # for each bit position from 0 to 23
            count = 0
            for num in candidates:
                # Check if the bit-th bit is set in the current number
                if num & (1 << bit):
                    count += 1
            # Track the largest combination size
            max_combination_size = max(max_combination_size, count)

        return max_combination_size
