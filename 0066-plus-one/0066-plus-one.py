class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join(map(str, digits))
        val = int(s) + 1
        res = list(map(int, str(val)))
        return res


        