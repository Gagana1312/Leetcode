class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"
    
        while len(word) < k:
            for c in word:
                new_part = ''.join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
                word += new_part
        
        return word[k - 1]
        