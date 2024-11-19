class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        res = arr[::-1]
        return " ".join(res)
        