class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        
        negative_result = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = dividend // divisor
        if negative_result:
            result = -result
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        return min(max(result, MIN_INT), MAX_INT)
        
        