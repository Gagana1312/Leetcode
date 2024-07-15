class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Supposed to use linkedList
        unique= set()
        res =0
        for n in nums:
            if n not in unique:
                unique.add(n)
            else:
                return n

        
        
        


        

        