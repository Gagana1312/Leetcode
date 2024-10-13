class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Min-heap to store (value, list_index, element_index)
        min_heap = []
        current_max = float('-inf')

        # Initialize the heap with the first element of each list and track the initial max element
        for i in range(len(nums)):
            value = nums[i][0]
            heapq.heappush(min_heap, (value, i, 0))
            current_max = max(current_max, value)

        # Initialize the smallest range as [min, max]
        smallest_range = [float('-inf'), float('inf')]

        while min_heap:
            # Pop the smallest element from the heap
            min_value, list_index, element_index = heapq.heappop(min_heap)

            # Update the range if the current one is smaller
            if current_max - min_value < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_value, current_max]

            # If there are more elements in the current list, push the next element into the heap
            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                # Update the current max since we've added a new element
                current_max = max(current_max, next_value)
            else:
                # If any list is exhausted, break the loop
                break

        return smallest_range
            