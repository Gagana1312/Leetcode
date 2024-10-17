class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        
        last_occurrence = {int(d): i for i, d in enumerate(digits)}
        
        for i in range(len(digits)):
            for d in range(9, int(digits[i]), -1):
                if last_occurrence.get(d, -1) > i:
                    j = last_occurrence[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        
        return num



        