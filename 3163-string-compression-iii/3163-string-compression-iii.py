class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0

        while i < len(word):
            # Get the current character
            current_char = word[i]
            count = 0

            # Count the number of consecutive occurrences of the current character
            while i < len(word) and word[i] == current_char and count < 9:
                count += 1
                i += 1

            # Append the count and the character to the result
            comp += str(count) + current_char

        return comp