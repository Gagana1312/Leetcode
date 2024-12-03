class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        res = []
        spaces_set = set(spaces)  
        for i, ch in enumerate(s):
            if i in spaces_set:
                res.append(" ")
            res.append(ch)
        return ''.join(res)

        