class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, countText[c] //balloon[c])
        return res
                
        