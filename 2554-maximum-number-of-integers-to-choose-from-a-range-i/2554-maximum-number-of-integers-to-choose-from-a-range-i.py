class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned) 
        current_sum = 0
        count = 0
        
        for i in range(1, n + 1): 
            if i not in banned_set and current_sum + i <= maxSum:
                current_sum += i
                count += 1
        
        return count
            
            
            


        