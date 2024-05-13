class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # countText = Counter(text)
        # balloon = Counter("balloon")

        # res = len(text)  # or float("inf")
        # for c in balloon:
        #     res = min(res, countText[c] // balloon[c])
        # return res

        return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))

                
        