class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 for base case
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Pop the last '(' index or -1
                if stack:
                    # Calculate valid length
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)  # Push the index of unmatched ')'

        return max_length
        