class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = set()

        for n in nums:
            if n in numbers:
                return True
            numbers.add(n)
        return False
        
        