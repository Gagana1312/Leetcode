class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # gifts.sort(reverse=True)
        # for i in range(k):
        #     gifts[0] = int(gifts[0] ** 0.5)
        #     gifts.sort(reverse=True)
        # return sum(gifts)
        
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        while k > 0 and max_heap:
            largest = -heapq.heappop(max_heap)
            reduced = math.floor(largest ** 0.5)
            heapq.heappush(max_heap, -reduced)
            k -= 1

        return int(-sum(max_heap))