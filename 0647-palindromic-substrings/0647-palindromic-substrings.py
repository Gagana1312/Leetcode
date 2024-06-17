class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = 0
        res =0

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                sol+=1
                l-=1
                r+=1
                

            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                sol+=1
                l-=1
                r+=1
        return sol

    #     sol = 0
    #     for i in range(len(s)):
    #         l,r=i,i
    #         sol += self.countPali(s, l , r)
    #         l,r=i,i+1
    #         sol += self.countPali(s, l , r)
    #     return sol

    # def countPali(self, s, l, r):
    #     sol=0
    #     while l>=0 and r<len(s) and s[l]==s[r]:
    #         sol+=1
    #         l-=1
    #         r+=1
    #     return sol



        