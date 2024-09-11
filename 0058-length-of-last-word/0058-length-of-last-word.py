class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()  # Splits the sentence into words
        # length=0
        # for word in words:
        #     length = len(word)
        # return length
        return len(words[-1])
        