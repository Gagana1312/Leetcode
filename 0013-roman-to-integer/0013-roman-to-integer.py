class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        rv = {"I":1,"V": 5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        for i in range(len(s)):
            if i<len(s)-1 and rv[s[i]] < rv[s[i+1]]:
                sum-=rv[s[i]]
                i+=1
            else:
                sum+=rv[s[i]]
        return sum
                

        
        