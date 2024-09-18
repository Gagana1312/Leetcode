class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # hp = set()
        # count = 0
        # l =0

        # for r in range(len(s)):
        #     while s[r] in hp:
        #         hp.remove(s[l])
        #         l+=1
        #     hp.add(s[r])
        #     count = max (count,r-l+1)
        # return count

        l=0
        longest=0
        dup =set()
        n = len(s)

        for r in range(n):
            while s[r] in dup:
                dup.remove(s[l])
                l+=1
            w =(r-l)+1
            longest = max(longest, w)
            dup.add(s[r])
        return longest
                