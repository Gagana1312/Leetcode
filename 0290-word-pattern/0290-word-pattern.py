class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(pattern)!=len(words):
            return False
        
        cw = {}
        wc = {}
        for c, w in zip(pattern, words):
            if c in cw and cw[c]!=w:
                return False
            if w in wc and wc[w]!=c:
                return False
            cw[c]=w
            wc[w]=c
        return True
