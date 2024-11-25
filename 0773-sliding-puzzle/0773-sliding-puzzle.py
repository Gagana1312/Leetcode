class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # Helper function to get possible moves from a given state
        def get_moves(state):
            moves = []
            zero_pos = state.index(0)
            if zero_pos % 3 > 0:
                moves.append(state[:zero_pos - 1] + [0, state[zero_pos - 1]] + state[zero_pos + 1:])
            if zero_pos % 3 < 2:
                moves.append(state[:zero_pos] + [state[zero_pos + 1], 0] + state[zero_pos + 2:])
            if zero_pos >= 3:
                moves.append(state[:zero_pos - 3] + [0] + state[zero_pos - 2:zero_pos] + [state[zero_pos - 3]] + state[zero_pos + 1:])
            if zero_pos < 3:
                moves.append(state[:zero_pos] + [state[zero_pos + 3]] + state[zero_pos + 1:zero_pos + 3] + [0] + state[zero_pos + 4:])
            return moves

        # Initial state and target state
        initial_state = [num for row in board for num in row]
        target_state = [1, 2, 3, 4, 5, 0]

        # BFS
        queue = deque([(initial_state, 0)])
        visited = set([tuple(initial_state)])
        while queue:
            state, moves = queue.popleft()
            if state == target_state:
                return moves
            for move in get_moves(state):
                if tuple(move) not in visited:
                    visited.add(tuple(move))
                    queue.append((move, moves + 1))

        return -1
            