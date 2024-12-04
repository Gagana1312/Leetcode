class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i, j = 0, 0
        
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  
            i += 1  
        return j == len(str2)
            
        
        
        