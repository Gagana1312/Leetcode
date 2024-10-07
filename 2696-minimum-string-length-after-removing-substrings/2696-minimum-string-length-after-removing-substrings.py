class Solution(object):
    def minLength(self, s):
        stack = []
        for char in s:
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack)
                
        