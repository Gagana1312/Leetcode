class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res =[]
        for i in operations:
            if i.lstrip('-').isdigit():
                res.append(int(i))
            elif i == 'C' and len(res)>=1:
                res.pop()
            elif i == 'D' and len(res)>=1:
                prod = 2*res[-1]
                res.append(prod)
            elif i == '+' and len(res)>=2:
                i= res[-1]
                j= res[-2]
                summ = i+j
                res.append(summ)
            
        return sum(res)


        