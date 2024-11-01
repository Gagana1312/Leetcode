class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize an empty result list
        result = []

        for char in s:
            # If the last two characters in result are the same as the current character, skip this character
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            # Otherwise, add the character to the result
            result.append(char)

        # Join the result list to form the final string and return it
        return ''.join(result)
