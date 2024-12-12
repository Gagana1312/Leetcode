class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        gifts.sort(reverse=True)
        for i in range(k):
            gifts[0] = int(gifts[0] ** 0.5)
            gifts.sort(reverse=True)
        return sum(gifts)