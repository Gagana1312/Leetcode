class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], x[1]))

        # Min-heap to track the end points of groups
        heap = []
            
        for interval in intervals:
            start, end = interval
            
            # If the current interval does not overlap with the earliest ending group
            if heap and start > heap[0]:
                heapq.heappop(heap)  # Remove the earliest ending group
            
            # Add the current interval's end to the heap (new group or updated group)
            heapq.heappush(heap, end)
        
        # The number of groups is the size of the heap
        return len(heap)
                