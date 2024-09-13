class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        Roman_Values = {"I":1,"V": 5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            
            if i < len(s) - 1 and Roman_Values[s[i]] < Roman_Values[s[i + 1]]:
                sum= sum- Roman_Values[s[i]]
                i+=1
            else:
                sum=sum+ Roman_Values[s[i]]

        return sum






        