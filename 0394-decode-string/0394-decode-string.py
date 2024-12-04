class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk =[]
        res=""
        
        for i in range(len(s)):
            if s[i]!="]":
                stk.append(s[i])
            else:
                substr =""
                while stk[-1]!="[":
                    substr = stk.pop()+substr
                stk.pop()
                k=""
                while stk and stk[-1].isdigit():
                    k=stk.pop()+k
                stk.append(int(k)*substr)

        return "".join(stk)

                
                
            


        