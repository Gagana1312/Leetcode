class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        for c in s:
            if c == '(':
                stk.append(c)  
            elif c == ')':
                if stk and stk[-1] == '(': 
                    stk.pop()
                else:
                    stk.append(c)  
        return len(stk)