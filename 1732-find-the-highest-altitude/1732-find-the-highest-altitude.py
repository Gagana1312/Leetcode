class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res =[0]

        for n in gain:
            x= res[-1]+n
            res.append(x)
        return max(res)
        