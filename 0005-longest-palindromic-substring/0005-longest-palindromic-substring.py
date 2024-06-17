class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol = ''
     

        for i in range(len(s)):
            #odd length
            l, r =i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1]) >= len(sol):
                    sol = s[l: r+1]
                l-=1
                r+=1
            
            #odd lenght
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1])>=len(sol):
                    sol=s[l:r+1]
                l-=1
                r+=1
        return sol


        