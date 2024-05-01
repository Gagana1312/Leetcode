class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapAB, mapBA = {},{}

        for i in range(len(s)):
            ch1,ch2 = s[i],t[i]
            if ((ch1 in mapAB and mapAB[ch1]!=ch2 or 
                ch2 in mapBA and mapBA[ch2]!=ch1)):
                return False
            mapAB[ch1]=ch2
            mapBA[ch2]=ch1
        return True

            
        
        