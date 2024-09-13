class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        substring_count = Counter(ransomNote)
        main_string_count = Counter(magazine)
        for char, count in substring_count.items():
            if main_string_count[char] < count:
                return False
        return True

        
         
        