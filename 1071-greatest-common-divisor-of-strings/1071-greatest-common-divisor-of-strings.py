class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # if len(str2)>len(str1):
        #     return ""
        # if str2 not in str1:
        #     return ""
        # else:
        #     return str1[len(str2):]

        # def isdivisor(l):
        #     if len1%l or len2%l:
        #         return False
        #     f1,f2 = len1 // l, len2 // l
        #     return str1[:l]*f1 == str1 and str1[:l]*f2 == str2

        # len1,len2 = len(str1),len(str2)
        # for l in range(min(len1,len2),0,-1):
        #     if isdivisor(l):
        #         return str1[:l]
        # return ""


        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
        
            
        