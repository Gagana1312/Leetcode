class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        for c1,c2 in zip(word1,word2):
            res=res+c1+c2
        if len(word1)>len(word2):
            res=res+word1[len(word2):]
        elif len(word2)>len(word1):
            res=res+word2[len(word1):]
        return res


        