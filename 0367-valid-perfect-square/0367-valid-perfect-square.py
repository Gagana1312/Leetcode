class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 0, num
        while start<=end:
            mid = (start+end )//2
            val = mid*mid
            if num == val:
                return True
            elif num>val:
                start= mid+1
            else:
                end=mid-1
        return False
        

        #return ((int(num ** 0.5))*(int(num**0.5))) == num