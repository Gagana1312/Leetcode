class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # l = 0
        # longest = 0
        # numberRep = 0
        # freq_map = {}  # Track the frequency of characters
        
        # n = len(s)
        # for r in range(n):
        #     # Update frequency map for the current character
        #     freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            
        #     # Update the number of replacements needed
        #     numberRep = (r - l + 1) - max(freq_map.values())
            
        #     # If replacements needed exceed k, shrink the window
        #     while numberRep > k:
        #         freq_map[s[l]] -= 1
        #         l += 1
        #         numberRep = (r - l + 1) - max(freq_map.values())
            
        #     # Calculate the longest valid window
        #     w = r - l + 1
        #     longest = max(longest, w)
        
        # return longest

        # window =0
        # numzeros = 0
        # n = len(s)
        # l=0
        # sett=set()
        # for r in range(n):
        #     if s[r] not in sett:
        #         numzeros +=1
        #         sett.add(s[l])
        #     while numzeros>k:
        #         if s[l] in sett:
        #             numzeros-=1
        #         l+=1
        #     w = r-l+1
        #     window = max(window,w)
        # return window


        longest =0
        l=0
        counts=[0]*26
        for r in range(len(s)):
            counts[ord(s[r])- 65]+=1
            while (r-l+1)-max(counts)>k:
                counts[ord(s[l])- 65]-=1
                l+=1
            longest = max(longest, (r-l+1))
        return longest


        
        







    
        