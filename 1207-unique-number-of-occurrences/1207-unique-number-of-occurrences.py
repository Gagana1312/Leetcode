class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr) 
        unique = set()  
        for c in count.values():  
            if c in unique: 
                return False
            unique.add(c)  
        return True 
        