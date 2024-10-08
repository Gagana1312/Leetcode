class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        max_unbalanced = 0
        for ch in s:
            if ch == '[':
                balance += 1  
            else:
                balance -= 1  
            max_unbalanced = min(max_unbalanced, balance)
        return (-max_unbalanced + 1) // 2