class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res=0
        j = set(jewels)
        for c in stones:
            if c in j:
                res+=1
        return res            