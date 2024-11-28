class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])

        # Define possible movement directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Min-heap to track paths with the least obstacles
        min_heap = []
        heappush(min_heap, (grid[0][0], 0, 0))  # (current_cost, x, y)

        # 2D array to store minimum obstacles for each cell
        obstacle_count = [[float('inf')] * cols for _ in range(rows)]
        obstacle_count[0][0] = grid[0][0]

        # Process paths using the min-heap
        while min_heap:
            current_cost, current_x, current_y = heappop(min_heap)

            # Check if reached bottom-right corner
            if current_x == rows - 1 and current_y == cols - 1:
                return current_cost

            # Explore adjacent cells
            for dx, dy in directions:
                next_x, next_y = current_x + dx, current_y + dy

                # Skip out-of-bounds cells
                if 0 <= next_x < rows and 0 <= next_y < cols:
                    # Calculate cost of moving to the next cell
                    next_cost = current_cost + grid[next_x][next_y]

                    # Update if new path has fewer obstacles
                    if next_cost < obstacle_count[next_x][next_y]:
                        obstacle_count[next_x][next_y] = next_cost
                        heappush(min_heap, (next_cost, next_x, next_y))

        # Return minimum obstacles to reach bottom-right corner
        return obstacle_count[rows - 1][cols - 1]
