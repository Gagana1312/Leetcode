class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        res =0

        for r in range(len(s)):
            if s[r]=="0":
                res += (r-l)
                l+=1

        return res
        
        
        

        