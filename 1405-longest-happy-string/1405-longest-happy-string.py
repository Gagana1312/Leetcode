class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # Max-heap: (negative_count, char)
        max_heap = []
        
        # Push the counts and characters to the heap, but only if the count > 0
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = []
        
        while max_heap:
            # Get the character with the most remaining occurrences
            first_count, first_char = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                # If adding this character would result in three consecutive identical characters
                if not max_heap:
                    break  # No other characters left to use
                
                # Use the second most frequent character instead
                second_count, second_char = heapq.heappop(max_heap)
                result.append(second_char)
                second_count += 1  # Decrease count (remember it's negative)
                
                # If the second character still has remaining occurrences, push it back to the heap
                if second_count < 0:
                    heapq.heappush(max_heap, (second_count, second_char))
                
                # Push the first character back to the heap since we skipped it
                heapq.heappush(max_heap, (first_count, first_char))
            else:
                # If it's safe to use the most frequent character
                result.append(first_char)
                first_count += 1  # Decrease count (remember it's negative)
                
                # If the character still has remaining occurrences, push it back to the heap
                if first_count < 0:
                    heapq.heappush(max_heap, (first_count, first_char))
        
        return "".join(result)
            