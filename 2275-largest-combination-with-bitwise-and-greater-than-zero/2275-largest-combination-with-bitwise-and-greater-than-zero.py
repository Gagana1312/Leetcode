class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        max_combination_size = 0
        for bit in range(24): 
            count = 0
            for num in candidates:
                if num & (1 << bit):
                    count += 1
            max_combination_size = max(max_combination_size, count)
        return max_combination_size
