class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest = max(candies)
        res =[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= largest:
                res.append(True)
            else:
                res.append(False)
        return res
        
        