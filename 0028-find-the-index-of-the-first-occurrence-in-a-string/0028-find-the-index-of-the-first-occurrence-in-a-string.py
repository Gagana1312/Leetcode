class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # ptr_s, ptr_n = 0,0
        # while ptr_s<= len(haystack):
        #     if haystack[ptr_s:len(needle)] == needle:
        #         return ptr_s
        #     ptr_s+=1
        # ptr_n+=1
        # return -1
        if not needle:
            return 0
        for ptr_s in range(len(haystack) - len(needle) + 1):
            if haystack[ptr_s:ptr_s + len(needle)] == needle:
                return ptr_s
        return -1


        