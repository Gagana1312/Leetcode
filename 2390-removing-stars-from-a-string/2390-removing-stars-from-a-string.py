class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res =[]

        for ch in s:
            if ch!="*":
                res.append(ch)
            elif len(res)>0:
                res.pop()
        return ''.join(res)
            
        