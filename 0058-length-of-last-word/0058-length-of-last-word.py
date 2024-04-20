class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        words = s.split()  # Splits the sentence into words
        length=0
        for word in words:
            length = len(word)
        
        return length


        #  return len(s.split()[-1])






        