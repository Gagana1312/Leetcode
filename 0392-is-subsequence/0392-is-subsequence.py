class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ptr_s, ptr_t = 0,0
        m= len(s)
        n= len(t)


        while ptr_s<m and ptr_t<n:
            if s[ptr_s] == t[ptr_t]:
                ptr_s+=1
            ptr_t+=1
        return ptr_s== m
        