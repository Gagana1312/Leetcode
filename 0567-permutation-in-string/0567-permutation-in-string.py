class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #works for only 2 char
        # revstring = s1[::-1]
        # if s1 in s2 or revstring in s2:
        #     return True
        # return False

        # if len(s1)>len(s2):
        #     return False
        
        #neetcode
        # s1Count, s2Count =[0]*26,[0]*26
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord('a')]+=1
        #     s2Count[ord(s2[i]) - ord('a')]+=1
        # matches =0
        # for i in range(26):
        #     matches+=(1 if s1Count[i]==s2Count[i] else 0)
        
        # left = 0
        # for right in range(len(s1),len(s2)):
        #     if matches == 26: return True

        #     index = ord(s2[right])- ord('a')
        #     s2Count[index]+=1
        #     if s1Count[index] == s2Count[index]:
        #         matches+=1
        #     elif s1Count[index]+1 == s2Count[index]:
        #         matches-=1

        #     index = ord(s2[left])- ord('a')
        #     s2Count[index]-=1
        #     if s1Count[index] == s2Count[index]:
        #         matches+=1
        #     elif s1Count[index]-1 == s2Count[index]:
        #         matches-=1
        #     left+=1
        

        # return matches == 26

        s1 = sorted(s1)
        for ptr in range(0,len(s2)-len(s1)+1):
            if (s2[ptr] in s1):
                if (sorted(s2[ptr:ptr+len(s1)]) == s1):
                    return True
        return False
        
            







        