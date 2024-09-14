class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        for c in tokens:
            if c.lstrip('-').isdigit(): 
                res.append(int(c))  
            elif c == "+" and len(res) >= 2:
                i = res.pop()
                j = res.pop()
                res.append(j + i)
            elif c == "-" and len(res) >= 2:
                i = res.pop()
                j = res.pop()
                res.append(j - i)
            elif c == "/" and len(res) >= 2:
                i = res.pop()
                j = res.pop()
                res.append(int(float(j) / i))
            elif c == "*" and len(res) >= 2:
                i = res.pop()
                j = res.pop()
                res.append(j * i)
        return res[0] 